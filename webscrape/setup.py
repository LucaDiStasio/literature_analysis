#!/usr/bin/env python

from distutils.core import setup

setup(name='webscrape',
      version='0.1',
      description='Thematic analysis of scientific literature: tools for web scraping',
      url='http://github.com/LucaDiStasio/literature_analysis/webscrape',
      author='Luca Di Stasio',
      author_email='luca.distasio@gmail.com',
      license='GNU GPL',
      packages=['webscrape'],
      install_requires=[
          'mechanize',
          'urllib',
          'urllib2',
          'cookielib',
          'BeautifulSoup',
          'random',
      ],
      zip_safe=False,
      keywords = ["scraping", "web scraping"],
      classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Development Status :: 0.1",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: Windows",
        "Topic :: Web Scraping :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
      long_description = """\
Web scraping tools
-------------------------------------

This version requires Python 2 or later.
""")