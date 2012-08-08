from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='misitio.portlet',
      version=version,
      description="portlet de desarrollo para el curso con @macagua",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='portlet ejemplos curso',
      author='Heber Bastidas',
      author_email='hbastidas@vtv.gob.ve',
      url='https://github.com/hbastidas/misitio.portlet',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['misitio'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
