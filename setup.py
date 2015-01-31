import itertools
import re

from collections import OrderedDict
from distutils.core import Command

from setuptools import setup

def dict_to_str(d, indent=0):
    prefix = ''.join(itertools.repeat(' ', indent))
    it = iter(d)
    key = next(it)
    lines = ['{{{0}: {1}'.format(key, d[key])]
    pattern = prefix + ' {0}: {1}'
    for key in it:
        lines.append(pattern.format(key, d[key]))
    lines[-1] = lines[-1] + '}'
    return '\n'.join(lines)

class parse_header(Command):
    user_options = [('where=', None, 'Path to the FreeImage.h header file.')]

    def initialize_options(self):
        print('Initializing options...')
        self.where = None

    def finalize_options(self):
        print('Finalizing options...')
        print(self.where)

    def run(self):
        pattern = re.compile('\s*(FIF_\S+)\s*=\s*([^,\n]*)')
        image_format = OrderedDict()

        with open(self.where, 'r', encoding='latin-1') as f:
            for line in f:
                result = pattern.match(line)
                if result is not None:
                    key = result.group(1)
                    try:
                        value = int(result.group(2))
                    except ValueError:
                        value = image_format[result.group(2)]
                    image_format[key] = value

        with open('./pyfreeimage/constants.py', 'w') as f:
            f.write('image_format = ' + dict_to_str(image_format,
                                                    indent=15) + '\n')


setup(name='pyfreeimage',
      version='0.0',
      description='ctypes wrapper around the FreeImage library',
      author='Sébastien Brisard',
      packages=['pyfreeimage'],
      cmdclass={'parse_header': parse_header})
