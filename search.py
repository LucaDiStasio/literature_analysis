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
from time import strftime
from random import randint

def init_json(outfilename,source,query):
   # Initialize output file
   today = strftime("%Y-%m-%d")
   now = strftime("%H-%M-%S")
   if outfilename != "":
      pathJSON = today + "_" + outfilename + ".json"
   else:
      pathJSON = today + "_mendeley_search.json"
   with codecs.open(pathJSON,'w','utf-8') as json:
      print ''
      print 'Creating json file: ' + str(json)
      print ''
      json.write('{\n')
      json.write('    "corpus": {\n')
      json.write('        "title": "' + 'THEMATIC ANALYSIS OF SCIENTIFIC LITERATURE' + '",\n')
      json.write('        "source": "' + source + '",\n')
      json.write('        "query": "' + query + '",\n')
      json.write('        "date": "' + today + '",\n')
      json.write('        "time": "' + now + '",\n')
      json.write('        "entries": {\n')
      json.write('                   },\n')
      json.write('        "status":"end"\n')
      json.write('              }\n')
      json.write('}\n')

# pubs = [title, authors, publication, volume, issue, pages, year, doi, abstract, keywords]
def update_json(day,outfilename,pubs):
   if outfilename != "":
      pathJSON = day + "_" + outfilename + ".json"
   else:
      pathJSON = day + "_mendeley_search.json"
   # read json file and find point of insertion
   with codecs.open(pathJSON,'r','utf-8') as json:
      lines = json.readlines()
   newlines = []
   for line in lines:
      if '"status":"end"' in line:
         newlines.append('         "entry": {\n')
         newlines.append('          "entrytitle": "' + pubs[0] + '",\n')
         newlines.append('          "authors": "' + pubs[1] + '",\n')
         newlines.append('          "publication": "' + pubs[2] + '",\n')
         newlines.append('          "volume": "' + pubs[3] + '",\n')
         newlines.append('          "issues": "' + pubs[4] + '",\n')
         newlines.append('          "pages": "' + pubs[5] + '",\n')
         newlines.append('          "year": "' + pubs[6] + '",\n')
         newlines.append('          "doi": "' + pubs[7] + '",\n')
         newlines.append('          "abstract": "' + pubs[8] + '",\n')
         newlines.append('          "keywords": "' + pubs[9] + '",\n')
         authorsList = pubs[1].split(',')
         firstAuthor = authorsList[0].replace(' ','-')
         newlines.append('            "id": "' + firstAuthor + '-' + pubs[6] + '-' + str(randint(0, 100000)) + '",\n')
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
   print "                           PUBLICATIONS"
   print "----------------------------------------------------------------------"
   print "----------------------------------------------------------------------"

def update_screen(selectbrowser,count,maxpage,pubs):
   # print status to screen
   if selectbrowser:
      browser = "Chrome on Windows 7 64 bit"
   else:
      browser = "Firefox on Windows 7 64 bit"
   print "----------------------------------------------------------------------"
   print "PUBLICATION number " + str(count) + " out of " + maxpage + " retrieved using " + browser + " on " + strftime("%d/%m/%Y") + " at " + strftime("%H-%M-%S")
   print ""
   print pubs[0]
   print pubs[1]
   print pubs[2] + ' (' + pubs[6] + '), volume ' + pubs[3] + ', issue ' + pubs[4] + ', page(s) ' + pubs[5]
   print ""
   print "DOI: http://www.doi.org/" + pubs[7]
   print ""
   print pubs[8]
   print ""
   print pubs[9]
   print "----------------------------------------------------------------------"

def get_websites():
   websites= {0: '20',                        # dictionary length
              1:'https://www.google.com',
              2:'https://www.facebook.com/',
              3:'https://www.linkedin.com/',
              4:'https://www.researchgate.net/home',
              5:'http://www.polimi.it/',
              6:'https://www.ethz.ch/de.html',
              7:'http://www.drexel.edu/',
              8:'https://www.youtube.com/',
              9:'http://www.univ-lorraine.fr/',
              10:'https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal',
              11:'http://physics.wustl.edu/nd/event/qmcd09/Docs/intro.php',
              12:'http://www.tre.it/',
              13:'https://www1.sunrise.ch/',
              14:'http://moocs.epfl.ch/information',
              15:'http://www.epfl.ch/',
              16:'http://www.lemonde.fr/',
              17:'http://www.ilgiornale.it/',
              18:'http://www.corriere.it/',
              19:'http://www.larousse.fr/dictionnaires/francais',
              20:'https://www.blablacar.fr/'}
   return websites

def fool_website(count,mech):
   webs = get_websites()
   # fool the website
   if (count//500)%2 > 0 and (count//50)%2 > 0:
      if randint(0,100) > 50:
         time.sleep(randint(5,120))
      if randint(0,100) < 50:
         randompage = mech.open(webs[randint(1,int(webs[0]))])
         time.sleep(randint(5,120))
              
def init_browser(browser):
   # Browser
   mech = mechanize.Browser()
   
   # Enable cookie support for urllib2 
   cookiejar = cookielib.LWPCookieJar() 
   mech.set_cookiejar( cookiejar )
   
   # Broser options 
   mech.set_handle_equiv( True ) 
   mech.set_handle_gzip( True ) 
   mech.set_handle_redirect( True ) 
   mech.set_handle_referer( True ) 
   mech.set_handle_robots( False ) 
   mech.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
   
   if browser=='Chrome' or browser=='chrome' or browser=='google chrome' or browser=='Google Chrome':
      mech.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'),
                              ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                              ('Accept-Language', 'en-gb,en;q=0.5'),
                              ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
                              ('Proxy-Connection', 'keep-alive')]
   elif browser=='Firefox' or browser=='firefox' or browser=='mozilla firefox' or browser=='Mozilla Firefox':
      mech.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'),
                              ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                              ('Accept-Language', 'en-gb,en;q=0.5'),
                              ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),
                              ('Proxy-Connection', 'keep-alive')]
   #Configuring Proxies
   #br.set_proxies({'http':'127.0.0.1:8120'})
   return mech
   

def scrape_mendeley(url, string, outfilename, startpage):
   
   day = strftime("%Y-%m-%d")
   
   # Create url for the query
   query = url + string.replace(" ","+")
   
   init_json(outfilename,'mendeley',query)
   
   count = 0
   
   if startpage==0:
      page = 0
   else:
      page = startpage   
   
   firstmech = init_browser('chrome')
   secondmech = init_browser('firefox')
   
   main = firstmech.open(query)
   html = main.read()
   initmainsoup = BeautifulSoup(html)
   
   screen_header()
   
   pageitems = initmainsoup.body.find(id="wrapper").find(id="main-container").find(id="content-container").find(id="main-content").find('div',"pagemenu").ul.findAll('li')
   maxpage = pageitems[-1].text
   g = re.search('[0-9.]+', maxpage)  # capture the inner number only
   maxpage = g.group(0)
   
   while page < int(maxpage):
      # scrape the web page
      pagequery = query + "&page=" + str(page)
      page = page + 1
      selectbrowser = 1 # Chrome
      if randint(0,100) > 50:
         selectbrowser = 0 # Firefox
      if selectbrowser:
         pagemain = firstmech.open(pagequery)
      else:
         pagemain = secondmech.open(pagequery)
      pagehtml = pagemain.read().decode('utf-8', 'ignore')
      mainsoup = BeautifulSoup(pagehtml)
      if mainsoup.body.find(id="wrapper").find(id="main-container").find(id="content-container").find(id="main-content").find('ol') != None:
         for item in mainsoup.body.find(id="wrapper").find(id="main-container").find(id="content-container").find(id="main-content").find('ol').findAll('li'):
            pubs = []
            title = ""
            link = ""
            authors = ""
            publication = ""
            year = ""
            volume = ""
            issue = ""
            pages = ""
            doi = ""
            abstract = ""
            keywords = ""
            count = count + 1
            title = item.article.find('div',"item-info").find('div',"title").a.get("title")
            link = item.article.find('div',"item-info").find('div',"title").a.get("href").encode('utf8')
            for author in item.article.find('div',"item-info").find('div',"metadata").find('span',"authors").findAll('span',"author"):
               newauthor = author.text
               if authors != "":
                  authors = authors + ", " + newauthor
               else:
                  authors = authors + newauthor
            publication = item.article.find('div',"item-info").find('div',"metadata").find('span',"publication").text
            year = str(item.article.find('div',"item-info").find('div',"metadata").find('span',"year").text).replace("(","").replace(")","")
            itemurl = "https://www.mendeley.com" + link
            if selectbrowser:
               itempage = firstmech.open(itemurl)
            else:
               itempage = secondmech.open(itemurl)
            itemhtml = itempage.read().decode('utf-8', 'ignore')
            itemsoup = BeautifulSoup(itemhtml)
            if itemsoup.body.find('article').find(id="abstract-container") != None:
               abstract = itemsoup.body.find('article').find(id="abstract-container").p.text
            if itemsoup.body.find('article').find('ul',"identifiers-list") != None:
               for identifier in itemsoup.body.find('article').find('ul',"identifiers-list").findAll('li'):
                  if "DOI" in identifier.span.text or "doi" in identifier.span.text:
                     doi = identifier.a.text
            if itemsoup.body.find('article').find('div',"container-metadata") != None:
               for info in itemsoup.body.find('article').find('div',"container-metadata").findAll('span',"info"):
                  if "volume" in info.text or "Volume" in info.text:
                     volume = info.span.text
                  elif "issue" in info.text or "Issue" in info.text:
                     issue = info.span.text
                  elif "pages" in info.text or "Pages" in info.text:
                     pages = info.span.text
            if itemsoup.body.find('article').find(id="keywords-container") != None:
               for keyword in itemsoup.body.find('article').find(id="keywords-container").find('div',"tags-list").findAll('a',"tag"):
                  newkeyword = keyword.text
                  if keywords != "":
                     keywords = keywords + "; " + newkeyword
                  else:
                     keywords = keywords + newkeyword
         
            pubs = [title, authors, publication, volume, issue, pages, year, doi, abstract, keywords]
            
            update_screen(selectbrowser,count,maxpage,pubs)
            
            update_json(day,outfilename,pubs)
            
            fool_website(count,firstmech)

def scrape_elsevier(username, password, url, string):
   # Create url for the query
   query = url + string.replace(" ","+")
   
   init_json(outfilename,'mendeley',query)
   
   count = 0
   
   if startpage==0:
      page = 0
   else:
      page = startpage   
   
   firstmech = init_browser('chrome')
   secondmech = init_browser('firefox')
   
   main = firstmech.open(query)
   html = main.read()
   initmainsoup = BeautifulSoup(html)
   
   screen_header()
   

def main(argv):
   database = ''
   searchstring = ''
   outputfile = ''
   baseurl = ''
   username = ''
   password = ''
   page = 0
   try:
      opts, args = getopt.getopt(argv,"hd:s:o:u:p:pa:",["help","Help","data","database","searchstring","search","ofile","outfile","outputfile","username","user","password","pwd","page","Page"])
   except getopt.GetoptError:
      print 'test.py -d <database> -s <search string> -o <output file> -u <username> -p <password>  -pa <page>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-h", "--help","--Help"):
         print ''
         print ''
         print '*********************************************************************************'
         print '*                                                                               *'
         print '*               A tool for scientific literature analysis                       *'
         print '*                                                                               *'
         print '*                                 by                                            *'
         print '*                                                                               *'
         print '*                        Luca Di Stasio, 2016                                   *'
         print '*                                                                               *'
         print '*********************************************************************************'
         print ''
         print 'Program syntax:'
         print 'search.py -d <database> -s <search string> -o <output file> -u <username> -p <password> -pa <page>'
         print ''
         print 'Mandatory arguments:'
         print '-d <database> -s <search string>'
         print ''
         print 'Optional arguments:'
         print '-o <output file> -u <username> -p <password> -pa <page>'
         print ''
         print 'Available databases:'
         print 'Database                                             Command-line option'
         print '--------------------------------------------------------------------------'
         print 'ACM Digital Library                                  ACM'
         print 'De Gruyter                                           De Gruyter'
         print 'DOAJ Directory of Open Access Journals               DOAJ'
         print 'GreenFile                                            GreenFile'
         print 'IEEE Xplore Digital Library                          IEEE'
         print 'Oxford Journals                                      Oxford Journals'
         print 'ScienceDirect Freedom (Elsevier)                     Elsevier'
         print 'SpringerLink                                         Springer'
         print 'Taylor & Francis                                     Taylor & Francis'
         print 'Techniques de l\'Ingenieur                            Techniques'
         print 'Wiley Online Library                                 Wiley'
         print 'WoS Web of Science                                   WoS'
         print 'Mendeley                                             Mendeley'
         print 'arXiv                                                arXiv'
         print ''
         sys.exit()
      elif opt in ("-d", "--data","--database"):
         database = arg
      elif opt in ("-s", "--searchstring","--search"):
         searchstring = arg
      elif opt in ("-o", "--ofile","--outfile","--outputfile"):
         outputfile = arg
      elif opt in ("-u", "--username","--user"):
         username = arg
      elif opt in ("-p", "--password","--pwd"):
         password = arg
      elif opt in ("-pa", "--page","--Page"):
         page = int(arg)
         
   if database=="Elsevier":
       baseurl = "http://www.sciencedirect.com.bases-doc.univ-lorraine.fr/"
   elif database=="Springer":
       baseurl = "http://link.springer.com.bases-doc.univ-lorraine.fr/"
   elif database=="WoS":
       baseurl = "http://apps.webofknowledge.com.bases-doc.univ-lorraine.fr/"
   elif database=="ACM":
       baseurl = "http://dl.acm.org.bases-doc.univ-lorraine.fr/"
   elif database=="De Gruyter":
       baseurl = "http://www.degruyter.com.bases-doc.univ-lorraine.fr/"
   elif database=="DOAJ":
       baseurl = "https://doaj.org/"
   elif database=="GreenFile":
       baseurl = "http://web.b.ebscohost.com.bases-doc.univ-lorraine.fr/ehost/"
   elif database=="IEEE":
       baseurl = "http://ieeexplore.ieee.org.bases-doc.univ-lorraine.fr/search/"
   elif database=="Oxford Journals":
       baseurl = "http://services.oxfordjournals.org.bases-doc.univ-lorraine.fr/cgi/"
   elif database=="Taylor & Francis":
       baseurl = "http://www.tandfonline.com.bases-doc.univ-lorraine.fr/action/"
   elif database=="Techniques":
       baseurl = "http://www.techniques-ingenieur.fr.bases-doc.univ-lorraine.fr/"
   elif database=="Wiley":
       baseurl = "http://onlinelibrary.wiley.com.bases-doc.univ-lorraine.fr/"
   elif database=="Mendeley":
       baseurl = "https://www.mendeley.com/research-papers/search/?query="
   elif database=="arXiv":
       baseurl = "http://arxiv.org/find/all/"
   else:
       baseurl = "www.google.com"
   
   #scrape_elsevier(username, password, baseurl, string)
   scrape_mendeley(baseurl, searchstring, outputfile, page)

if __name__ == "__main__":
   main(sys.argv[1:])