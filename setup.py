from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(name='ctci',
      version='1.0',
      description='Cracking the Coding Interview, 5th Edition',
      author='Ximura',
      author_email='',
      url='',
      packages=find_packages(exclude=['test', 'test.*']),
      python_requires='>=3.6',
      install_requires=install_requires
      )
