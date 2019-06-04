from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='korr',
      version='0.8.0',
      description='collection of utility functions for correlation analysis',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/kmedian/korr',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['korr'],
      install_requires=[
          'setuptools>=40.0.0',
          'nose>=1.3.7',
          'numpy>=1.14.5',
          'scipy>=1.1.0',
          'pandas>=0.23.4',
          'matplotlib>=3.0.0'],
      python_requires='>=3.6',
      zip_safe=False)
