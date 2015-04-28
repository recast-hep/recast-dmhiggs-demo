from setuptools import setup, find_packages

setup(
  name = 'recast-dmhiggs-demo',
  version = '0.0.1',
  description = 'recast-dmhiggs-demo',
  url = 'http://github.com/recast-hep/recast-dmhiggs-demo',
  author = 'Lukas Heinrich',
  author_email = 'lukas.heinrich@cern.ch',
  packages = find_packages(),
  include_package_data = True,
  install_requires = [
    'Flask',
    'yoda',
    'pyyaml',
    'adage',
    'click'
  ],
    entry_points = {
        'console_scripts': ['recastworkflow-dmhiggs=recastdmhiggs.recastworkflowcli:run_workflow'],
    },
    dependency_links = [
    'https://github.com/lukasheinrich/adage/tarball/master#egg=adage-0.1.1',
  ]
)
