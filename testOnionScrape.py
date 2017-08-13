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

import socks
import socket
import stem.process
from stem import Signal
from stem.control import Controller
from splinter import Browser
import time
import sys, getopt, re, mechanize, urllib, urllib2, cookielib, os, csv, codecs
from BeautifulSoup import BeautifulSoup
from time import strftime
from random import randint
import requests

'''
def switchIP():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)

def init_browser():
    proxyIP = "127.0.0.1"
    proxyPort = 9150
    
    proxy_settings = {"network.proxy.type":1,
        "network.proxy.ssl": proxyIP,
        "network.proxy.ssl_port": proxyPort,
        "network.proxy.socks": proxyIP,
        "network.proxy.socks_port": proxyPort,
        "network.proxy.socks_remote_dns": True,
        "network.proxy.ftp": proxyIP,
        "network.proxy.ftp_port": proxyPort
    }
    browser = Browser('firefox', profile_preferences=proxy_settings)
    return browser

query = "http://www.eng-tips.com/viewthread.cfm?qid=274802"

browser = init_browser()

browser.visit(query)

html = browser.html
initmainsoup = BeautifulSoup(html)

print(initmainsoup)
'''


SOCKS_PORT=9150# You can change the port number

tor_process = stem.process.launch_tor_with_config(
    tor_cmd = 'C:\\Program Files\\Tor Browser\\Browser\\TorBrowser\\Tor\\tor.exe',
    timeout = 600,
    config = {
        'SocksPort': str(SOCKS_PORT),
    }
)


socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5,
                      addr="127.0.0.1", 
                      port=SOCKS_PORT)
socket.socket = socks.socksocket




#Write your scraping code here -- I use BeautifulSoup for scraping

html = requests.get("http://www.eng-tips.com/viewthread.cfm?qid=274802").text
initmainsoup = BeautifulSoup(html)

print initmainsoup.body

tor_process.kill()

