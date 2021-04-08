from setuptools import setup
import pypandoc


def get_version(path):
    with open(path, "r") as fp:
        lines = fp.read()
    for line in lines.split("\n"):
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


setup(name='korr',
      version=get_version("korr/__init__.py"),
      description='collection of utility functions for correlation analysis',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/kmedian/korr',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['korr'],
      install_requires=[
          'setuptools>=40.0.0',
          'numpy>=1.14.5,<2',
          'scipy>=1.1.0,<2',
          'matplotlib>=3.3.0'],
      python_requires='>=3.6',
      zip_safe=True)
