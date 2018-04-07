from setuptools import setup, find_packages

setup(name='contact',
      version='0.1',
      description='Command line app for JSON contact list',
      url='https://github.com/jdoid/contact-cli',
      author='Dean Kirby',
      author_email='jdoid@fastmail.us',
      license='MIT',
      keywords='cli contacts json csv',
      packages=[
            'contact',
            'data',
      ],
      package_data={'': ['*.json']},
      include_package_data=True,
      zip_safe=False)