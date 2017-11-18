#! /usr/bin/env python2

"""

Title: Scraping the Web with BeautifulSoup
Author: Holm Smidt
Version: 0.9
Date: 11-11-2017

Overview:
* Simple script to use BeautifulSoup4 package for web scraping.
* The goal is to retriever weather and surf reports from various sites.
* Basic html understanding is recommended.

* Code adapted from: https://goo.gl/pCF51R
"""

import urllib2
from bs4 import BeautifulSoup
import numpy as np
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
import sys  # import sys package, if not already imported

reload(sys)
sys.setdefaultencoding('utf-8')


""" Example 1: Retrieve Surf Conditions """

# specify the url
url = 'http://www.surfline.com/surf-report/south-shore-overview-oahu_4761/'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(url)

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
wave_range_box = soup.find('h2', attrs={'id': 'observed-wave-range'})
wave_range = wave_range_box.text.strip() # strip() is used to remove starting and trailing

# get the observed spot conditions
spot_conditions_box = soup.find('div', attrs={'id':'observed-spot-conditions'})
spot_conditions = spot_conditions_box.text

# print results
print "***********************"
print "South Shore Surf Report"
print "Wave Range: ", wave_range
print "Spot Conditions: ", spot_conditions


""" Example 2: Pull weather data """


weather_url ='https://weather.com/weather/today/l/21.31,-157.86'
page = urllib2.urlopen(weather_url)
soup = BeautifulSoup(page, 'html.parser')

# find temperature
temperature_box = soup.find('div', attrs={'class':'today_nowcard-temp'})
temperature = temperature_box.text


#find other conditions
table = soup.find(text="Right Now").find_parent("table")

data = []
table_body = table.find('tbody')
#print table
#print table.body
rows = table_body.findAll('tr')
for row in rows:

    #just single column
    ele = row.find('td')
    print ele.text.strip()
    data.append((str(ele.text.strip())))

    #cols = row.findAll('td')
    #cols = [ele.text.strip() for ele in cols]
    #data.append([str(ele) for ele in cols if ele]) # Get rid of empty values


print "\n***********************"
print "Honolulu Weather Report"
print "Temperature: ", temperature, " F"
print "Wind: ", data[0]
print "Humidity: ", data[1]
print "Dew Point:  ", data[2].split("\xc2", 1)[0], " F"
print "Pressure: ", data[3]
print "Visibility: ", data[4]
