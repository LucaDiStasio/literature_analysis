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

import sys, getopt, re, mechanize, urllib, urllib2, cookielib, os, time, csv, codecs, webscrape
from BeautifulSoup import BeautifulSoup
from time import strftime
from random import randint

def init_json(language,outfilename,source,query):
   # Initialize output file
   today = strftime("%Y-%m-%d")
   now = strftime("%H-%M-%S")
   if outfilename != "":
      pathJSON = today + "_" + outfilename + ".json"
   else:
      pathJSON = today + "_" + language + "_dictionary.json"
   with codecs.open(pathJSON,'w','utf-8') as json:
      print ''
      print 'Creating json file: ' + str(json)
      print ''
      json.write('{\n')
      json.write('    "dictionary": {\n')
      json.write('        "title": "' + 'DICTIONARY' + '",\n')
      json.write('        "source": "' + source + '",\n')
      json.write('        "language": "' + language + '",\n')
      json.write('        "date": "' + today + '",\n')
      json.write('        "time": "' + now + '",\n')
      json.write('        "entries": {\n')
      json.write('        "status":"end"\n')
      json.write('                   }\n')
      json.write('              }\n')
      json.write('}\n')

# entry = [word,part-of-speech]
def newentry_json(day,language,outfilename,entry):
   if outfilename != "":
      pathJSON = today + "_" + outfilename + ".json"
   else:
      pathJSON = today + "_" + language + "_dictionary.json"
   # read json file and find point of insertion
   with codecs.open(pathJSON,'r','utf-8') as json:
      lines = json.readlines()
   newlines = []
   for line in lines:
      if '"status":"end"' in line:
         newlines.append('         "entry": {\n')
         newlines.append('          "mainform": "' + pubs[0] + '",\n')
         newlines.append('          "part-of-speech": "' + pubs[1] + '",\n')
         newlines.append('                  },\n')
         newlines.append(line)
      else:
         newlines.append(line)
   # re-write json file with new data
   with codecs.open(pathJSON,'w','utf-8') as json:
      for line in newlines:
         json.write(line)

def screen_header():
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"
   print "                              WORDS"
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"

def update_screen(selectbrowser,count,maxpage,pubs):
   # print status to screen
   if selectbrowser:
      browser = "Chrome on Windows 7 64 bit"
   else:
      browser = "Firefox on Windows 7 64 bit"
   print "----------------------------------------------------------------------"
   print "WORD number " + str(count) + " retrieved using " + browser + " on " + strftime("%d/%m/%Y") + " at " + strftime("%H:%M:%S")
   print ""
   print pubs[0] + ', ' + pubs[1]
   print ""
   print "----------------------------------------------------------------------"