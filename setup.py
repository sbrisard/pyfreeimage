import itertools
import re

from collections import OrderedDict
from distutils.core import Command
from functools import partial

from setuptools import setup


def format_key(key, prefix):
    """Return key, stripped of prefix and converted to lower case."""
    if prefix is None:
        return key
    if not(key.startswith(prefix)):
        raise ValueError('String \'{}\' does not '
                         'start with \'{}\'.'.format(key, prefix))
    else:
        return key[len(prefix):].lower()


def format_enum_name(name):
    """Convert C enum names to more pythonic names.

    Use camel-case, and remove 'FREE_IMAGE_' prefix.
    """
    prefix = 'FREE_IMAGE_'
    if name.startswith(prefix):
        tokens = name[len(prefix):].split('_')
        return ''.join(token.capitalize() for token in tokens)
    else:
        raise ValueError('Enum name should start with '
                         'FREE_IMAGE (got {})'.format(name))

def format_dict_keys(d, formatter=None):
    """Apply `formatter` to all keys of `d` and return a new dictionnary."""
    if formatter is None:
        def formatter(key):
            return key
    return OrderedDict((formatter(key), value) for key, value in d.items())


def parse_enum(header, prefix):
    """Return an enum defined in the header file as a dictionary.

    This function returns a dictionary of all constants defined in
    the header, whose name starts with `prefix`. `header` is the list
    of lines of the header file.

    """
    enum = OrderedDict()
    pattern = re.compile('\s*((' + prefix + ')_(\S+))\s*=\s*([^,\n\s]*)')
    for line in header:
        result = pattern.match(line)
        if result is not None:
            key, value = result.group(1), result.group(4)
            try:
                value = int(value)
            except ValueError:
                value = enum[value]
            enum[key] = value
    return enum

def parse_enums(header):
    """Return all `FI_ENUM` defined in the header.

    This function returns a dict of all enums. The keys are the C names
    of these enums. The values are dicts themselves.

    """
    begin_enum = re.compile('\s*FI_ENUM\((.*)\).*')
    end_enum = re.compile('\s*\}\s*;.*')
    enum_item = re.compile('\s*(\S+)\s*=\s*([^,\n\s]*)')
    enums = dict()
    enum = None
    for line in header:
        if enum is None:
            result = begin_enum.match(line)
            if result is not None:
                enum = OrderedDict()
                enums[result.group(1)] = enum
        else:
            # We are already parsing an enum
            if end_enum.match(line) is not None:
                # Have we reached the end yet?
                enum = None
            else:
                result = enum_item.match(line)
                if result is not None:
                    key, value = result.group(1), result.group(2)
                    try:
                        value = int(value)
                    except ValueError:
                        value = enum[value]
                    enum[key] = value
                else:
                    raise RuntimeError(line)
    return enums


def parse_constants(header):
    """Returns a dict of all constants defined in the header.

    Constants which cannot be parsed trivially are excluded from the
    returned dict. This is the case of constants defined through
    conditionals.

    """
    exclude = [re.compile(expr) for expr in ['FREEIMAGE_.*',
                                             'DLL_.*',
                                             'GCC.*',
                                             '_WINDOWS_.*',
                                             'SEEK.*',
                                             'FI_RGBA.*',
                                             'FI_DEFAULT.*',
                                             'FI_ENUM.*',
                                             'FI_STRUCT.*',
                                             'PLUGINS',
                                             'FI_COLOR_PALETTE_SEARCH_MASK']]

    constants = dict()
    pattern = re.compile('\s*#define\s*(\S+)\s*([^,\n\s]*)')
    for line in header:
        result = pattern.match(line)
        if (result is not None and
            all(p.match(result.group(1)) is None for p in exclude)):
            key, value = result.group(1), result.group(2)
            try:
                value = int(value, 0)
            except ValueError:
                value = constants[value]
            constants[key] = value
    return constants


def write_enum(f, name, members):
    """Write the Python code for the definition of one enum.

    `f` is the file to which the enum definition is to be written;
    `name` is the name the enum will be given in this file. `members`
    is a dictionary of `name: value` entries which define the members
    of the enum.

    """
    f.write('class {0}(Enum):\n'.format(name))
    for key, value in members.items():
        f.write('    {0} = {1}\n'.format(key, value))


def write_enums(f, names, members):
    """Write the python code for the definition of several enums.

    `f` is the file to which the enum definitions are to be written.
    `enum_names`, `enum_members` are two dictionaries sharing the same
    set of keys. Let `key` be one such common key. Then `names[key]` is
    the name the enum will be given in the file; `members[key]` is a
    dictionary of `name: value` entries wich define the members of the
    enum.

    """
    f.write('from enum import Enum\n')
    for prefix, name in names.items():
        f.write('\n\n')
        write_enum(f, name, members[prefix])


def parse_io_flags(header, fiformats):
    prefixes = [fiformat.upper() for fiformat in fiformats]
    extra = ['FIF_LOAD_NOPIXELS']
    pattern = re.compile('\s*#define\s*((' +
                         '|'.join(prefixes) +
                         ')_\S+|' +
                         '|'.join(extra) +
                         ')\s*([^,\n\s]*)')
    for line in header:
        result = pattern.match(line)
        if result is not None:
            print(result.group(1), result.group(3))


class parse_header(Command):
    user_options = [('where=', None, 'Path to the FreeImage.h header file.')]

    def initialize_options(self):
        self.where = None

    def finalize_options(self):
        pass

    def run(self):
        with open(self.where, 'r', encoding='latin-1') as f:
            header = f.readlines()
        enum_names = OrderedDict([('FIT', 'Type'), ('FIF', 'Format')])
        enum_members = OrderedDict()
        for prefix in enum_names.keys():
            formatter = partial(format_key, prefix=prefix + '_')
            enum_members[prefix] = format_dict_keys(parse_enum(header, prefix),
                                                    formatter)
        with open('./pyfreeimage/_constants.py', 'w') as f:
            write_enums(f, enum_names, enum_members)
        parse_io_flags(header, enum_members['FIF'].keys())


setup(name='pyfreeimage',
      version='0.0',
      description='ctypes wrapper around the FreeImage library',
      author='Sébastien Brisard',
      packages=['pyfreeimage'],
      cmdclass={'parse_header': parse_header})
