import itertools
import re

from collections import OrderedDict
from distutils.core import Command

from setuptools import setup


class parse_header(Command):
    user_options = [('where=', None, 'Path to the FreeImage.h header file.')]

    def initialize_options(self):
        self.where = None

    def finalize_options(self):
        pass

    def run(self):
        enum_names = {'FIF': 'Format', 'FIT': 'Type'}
        enum_members = self.parse_enums(enum_names.keys())
        with open('./pyfreeimage/_constants.py', 'w') as f:
            self.write_enums(f, enum_names, enum_members)


    def parse_enums(self, prefixes):
        dicts = dict((prefix, OrderedDict()) for prefix in prefixes)
        all_constants = dict()
        pattern = re.compile('\s*((' +
                             '|'.join(prefixes) +
                             ')_(\S+))\s*=\s*([^,\n\s]*)')

        with open(self.where, 'r', encoding='latin-1') as f:
            for line in f:
                result = pattern.match(line)
                if result is not None:
                    key = result.group(3).lower()
                    try:
                        value = int(result.group(4))
                    except ValueError:
                        value = all_constants[result.group(4)]
                    all_constants[result.group(1)] = value
                    dicts[result.group(2)][key] = value
        return dicts

    def write_enums(self, f, enum_names, enum_members):
        f.write('from enum import Enum\n')
        for prefix, enum_name in enum_names.items():
            f.write('\n\n')
            f.write('class {0}(Enum):\n'.format(enum_name))
            for item in enum_members[prefix].items():
                f.write('    {0} = {1}\n'.format(*item))


setup(name='pyfreeimage',
      version='0.0',
      description='ctypes wrapper around the FreeImage library',
      author='Sébastien Brisard',
      packages=['pyfreeimage'],
      cmdclass={'parse_header': parse_header})
