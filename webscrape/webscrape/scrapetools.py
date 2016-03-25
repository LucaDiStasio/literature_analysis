#!/usr/bin/env python

import mechanize, urllib, urllib2, cookielib
from BeautifulSoup import BeautifulSoup
from random import randint

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