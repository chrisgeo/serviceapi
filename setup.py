from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()
requires = open(os.path.join(here, 'requirements.txt')).read().splitlines()

version = os.environ.get('VERSION', 'dev')

setup(name='serviceapi',
      version=version,
      description="Variable Config API Endpoints",
      long_description="""\
Variable Config API Endpoints""",
      classifiers=[],
      keywords='serviceapi',
      author='Chris George',
      author_email='chris@leftronic.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      setup_requires=['setuptools_git'],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

