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

import stem.process
from stem import Signal
from stem.control import Controller
from splinter import Browser
import time

def switchIP():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        
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

'''
browser.visit("http://www.icanhazip.com")
'''
for x in range(10):
    browser.visit("http://www.icanhazip.com")
    switchIP()
    time.sleep(5)