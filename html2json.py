#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
=====================================================================================

Copyright (c) 2016 Université de Lorraine & Luleå tekniska universitet
Author: Luca Di Stasio <luca.distasio@gmail.com>
                       <luca.distasio@ingpec.eu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

=====================================================================================

DESCRIPTION


Tested with Python 2.7 Anaconda 2.4.1 (64-bit) distribution in Windows 7.

'''

import sys, getopt, re, mechanize, urllib, urllib2, cookielib, os, time, csv, codecs
from BeautifulSoup import BeautifulSoup
from random import randint


path = 'D:/01_Luca/03_DocMASE/04_WD/literature_analysis/'
filename1 = '2016_1_20_mendeley_search'
filename2 = '2016_1_21_mendeley_search'
filename3 = '2016_1_22_mendeley_search'

mech = mechanize.Browser()

filename = filename1
page = mech.open('file:///'+path+filename+'.html')
html = page.read().decode('utf-8', 'ignore')
soup = BeautifulSoup(html)

title = soup.header.h1.text
subtitle = soup.header.h2.text
source = soup.header.source.text
query = soup.header.query.text

with codecs.open(path+filename+'.json','w','utf-8') as json:
    json.write('{\n')
    json.write('    "corpus": {\n')
    json.write('        "title": "' + title + '",\n')
    json.write('        "source": "' + source + '",\n')
    json.write('        "query": "' + query + '",\n')
    json.write('        "date": "' + '2016-01-20' + '",\n')
    json.write('        "time": "' + ' ' + '",\n')
    json.write('        "entries": {\n')
    
for item in soup.body.ol.findAll('li'):
   with codecs.open(path+filename+'.json','a','utf-8') as json:
      json.write('         "entry": {\n')
      if item.find('p',"title") != None:
         title = item.find('p',"title").text
         json.write('            "entrytitle": "' + title + '",\n')
      if item.find('p',"authors") != None:
         authors = item.find('p',"authors").text
         json.write('            "authors": "' + authors + '",\n')
      if item.find('p',"publication") != None:
         publication = item.find('p',"publication").text
         json.write('            "publication": "' + publication + '",\n')
      if item.find('p',"volume") != None:
         volume = item.find('p',"volume").text
         json.write('            "volume": "' + volume + '",\n')
      issues = item.findAll('p',"issue")
      if len(issues)>1:
         if issues[0] != None:
               json.write('            "issues": "' + issues[0].text + '",\n')
         if issues[1] != None:
               json.write('            "pages": "' + issues[1].text + '",\n')
      else:
         if item.find('p',"issue") != None:
               issue = item.find('p',"issue").text
               json.write('            "issue": "' + issue + '",\n')
      if item.find('p',"year") != None:
         year = item.find('p',"year").text
         json.write('            "year": "' + year + '",\n')
      if item.find('p',"doi") != None:
         doi = item.find('p',"doi").text
         json.write('            "doi": "' + doi + '",\n')
      if item.find('p',"abstract") != None:
         abstract = item.find('p',"abstract").text
         json.write('            "abstract": "' + abstract + '",\n')
      if item.find('p',"keywords") != None:
         keywords = item.find('p',"keywords").text
         json.write('            "keywords": "' + keywords + '",\n')
      json.write('                  },\n')
 
with codecs.open(path+filename+'.json','a','utf-8') as json:
   json.write('                   }\n')
   json.write('              }\n')
   json.write('}\n')

filename = filename2
page = mech.open('file:///'+path+filename+'.html')
html = page.read().decode('utf-8', 'ignore')
soup = BeautifulSoup(html)

title = soup.header.h1.text
subtitle = soup.header.h2.text
source = soup.header.source.text
query = soup.header.query.text

with codecs.open(path+filename+'.json','w','utf-8') as json:
    json.write('{\n')
    json.write('    "corpus": {\n')
    json.write('        "title": "' + title + '",\n')
    json.write('        "source": "' + source + '",\n')
    json.write('        "query": "' + query + '",\n')
    json.write('        "date": "' + '2016-01-20' + '",\n')
    json.write('        "time": "' + ' ' + '",\n')
    json.write('        "entries": {\n')
    
for item in soup.body.ol.findAll('li'):
   with codecs.open(path+filename+'.json','a','utf-8') as json:
      json.write('         "entry": {\n')
      if item.find('p',"title") != None:
         title = item.find('p',"title").text
         json.write('            "entrytitle": "' + title + '",\n')
      if item.find('p',"authors") != None:
         authors = item.find('p',"authors").text
         json.write('            "authors": "' + authors + '",\n')
      if item.find('p',"publication") != None:
         publication = item.find('p',"publication").text
         json.write('            "publication": "' + publication + '",\n')
      if item.find('p',"volume") != None:
         volume = item.find('p',"volume").text
         json.write('            "volume": "' + volume + '",\n')
      issues = item.findAll('p',"issue")
      if len(issues)>1:
         if issues[0] != None:
               json.write('            "issues": "' + issues[0].text + '",\n')
         if issues[1] != None:
               json.write('            "pages": "' + issues[1].text + '",\n')
      else:
         if item.find('p',"issue") != None:
               issue = item.find('p',"issue").text
               json.write('            "issue": "' + issue + '",\n')
      if item.find('p',"year") != None:
         year = item.find('p',"year").text
         json.write('            "year": "' + year + '",\n')
      if item.find('p',"doi") != None:
         doi = item.find('p',"doi").text
         json.write('            "doi": "' + doi + '",\n')
      if item.find('p',"abstract") != None:
         abstract = item.find('p',"abstract").text
         json.write('            "abstract": "' + abstract + '",\n')
      if item.find('p',"keywords") != None:
         keywords = item.find('p',"keywords").text
         json.write('            "keywords": "' + keywords + '",\n')
      json.write('                  },\n')
 
with codecs.open(path+filename+'.json','a','utf-8') as json:
   json.write('                   }\n')
   json.write('              }\n')
   json.write('}\n')