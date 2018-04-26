from setuptools import setup, find_packages

setup(name='contacts_cli',
      version='0.2.0',
      description='Command line app for JSON contact list',
      url='https://github.com/jdoid/contact-cli',
      author='Dean Kirby',
      author_email='jdoid@fastmail.us',
      license='MIT',
      keywords='cli contacts json csv',
      packages=find_packages(),
      package_data={'data': ['data/*.json']},
      include_package_data=True,
      zip_safe=False)