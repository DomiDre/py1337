from setuptools import setup, find_packages

with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
  name='py1337',
  version='1.0.0',
  description='Post 1337 to an Whatsapp group at 13:37.',
  url='https://github.com/DomiDre/py1337',
  author='Dominique Dresen',
  author_email='dominiquedresen@gmail.com',
  license=license,
  long_description=readme,
  install_requires=[
    'selenium'
  ],
  python_requires='>2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
  platforms=['Linux'],
  package_dir={'py1337': 'py1337'},
  packages=find_packages(
    exclude=(
      '_build',
      'docs',
      '_static',
      '_templates'
      'tests',
      'examples'
      )
  ),
  keywords='whatsapp 1337'
)