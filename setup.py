from distutils.core import Command

from setuptools import setup

class parse_header(Command):
    user_options = [('where=', None, 'Path to the FreeImage.h header file.')]

    def initialize_options(self):
        print('Initializing options...')
        self.where = None

    def finalize_options(self):
        print('Finalizing options...')
        print(self.where)

    def run(self):
        print('running parse_header')

setup(name='pyfreeimage',
      version='0.0',
      description='ctypes wrapper around the FreeImage library',
      author='Sébastien Brisard',
      packages=['pyfreeimage'],
      cmdclass={'parse_header': parse_header})
