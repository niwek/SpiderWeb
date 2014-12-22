'''
Created on Dec 21, 2014

@author: KWL
'''

import urllib2
import urlutils
from bs4 import BeautifulSoup

BASE_URL = "https://www.webstaurantstore.com"

def get_base():
    links = []
    try:
        f =urllib2.urlopen(BASE_URL)
        soup = BeautifulSoup(f.read())
        for link in soup.find(id="product-categories").ul.find_all('li'):
            links.append(urlutils.formatUrl(link.a.get('href')))
        
    except urllib2.URLError:
        print "Error connection to: " + BASE_URL
    finally:
        f.close()
        
    return links

def get_level_one(url):
    links = []
    try:
        f =urllib2.urlopen(url)
        soup = BeautifulSoup(f.read())
        for link in soup.find_all(class_='grid-item grid-parent'):
            if link.name == 'span' and link.find('a'):
                links.append(urlutils.formatUrl(link.a.get('href')))
            elif link.name == 'a':
                links.append(urlutils.formatUrl(link.get('href')))
        
    except urllib2.URLError:
        print "Error connection to: " + url
    finally:
        f.close()
    
    return links

if __name__ == '__main__':
    pass