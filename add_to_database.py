#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt, re, mechanize, urllib, urllib2, cookielib, os, time, csv, codecs
from BeautifulSoup import BeautifulSoup
from datetime import datetime
from random import randint
from pymongo import MongoClient





def main(argv):
    
    # Read the command line, throw error if not option is provided
    try:
        opts, args = getopt.getopt(argv,'hD:x:y:z:t:o:d:',['help','Help','inputfile','input','dir','directory','data','database'])
    except getopt.GetoptError:
        print 'add_to_database.py -i <input file> -d <input directory> -D <database>'
        sys.exit(2)
    # Parse the options and create corresponding variables
    for opt, arg in opts:
        if opt in ('-h', '--help','--Help'):
            print ' '  
            print ' '  
            print '********************************************************************************* '  
            print ' '  
            print '                                     EUSMAT'  
            print '                         European School of Materials'  
            print ' '  
            print '                                     DocMASE'  
            print '                  DOCTORATE IN MATERIALS SCIENCE AND ENGINEERING'  
            print ' '  
            print ' '  
            print '       MECHANICS OF EXTREME THIN COMPOSITE LAYERS FOR AEROSPACE APPLICATIONS'  
            print ' '  
            print ' '  
            print '                         Differential geometry tools'  
            print ' '
            print '                         MongoDB database management'
            print ' '
            print '                                      by'  
            print ' '  
            print '                             Luca Di Stasio, 2016'  
            print ' '  
            print ' '  
            print '********************************************************************************* '  
            print ''
            print 'Program syntax:'
            print 'add_to_database.py -i <input file> -d <input directory> -D <database>'
            print ''
            print 'Mandatory arguments:'
            print '-i <input file> -d <input directory> -D <database>'
            print ''
            print 'Optional arguments:'
            print ''
            print ''
            print 'Available test cases:'
            print ''
            print ''
            sys.exit()
        elif opt in ("-i", "--inputfile", "--input"):
            inputfile = arg
        elif opt in ("-d", "--dir", "--directory"):
            inputdir = arg
        elif opt in ("-D", "--data", "--database"):
            database = arg
    
    # Check the existence of variables: if a required variable is missing, an error is thrown and program is terminated; if an optional variable is missing, it is set to the default value
    if 'inputfile' not in locals():
        print 'Error: input file not provided.'
        sys.exit(2)
    if 'inputdir' not in locals():
        print 'Error: input directory not provided.'
        sys.exit(2)
    if 'database' not in locals():
        print 'Error: database not provided.'
        sys.exit(2)



if __name__ == "__main__":
    main(sys.argv[1:])