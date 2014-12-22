'''
Created on Nov 16, 2014

@author: KWL
'''

import re
import urlutils
import urllib
import webstaurantstoreUtils
from bs4 import BeautifulSoup

NOT_GOOD = "^(.*?)(\.jpg|\.png)(.*?)$"

def testreplacehttps():
    url = "http://www.facebook.com"
    if url.startswith("http://"):
        print re.sub(r"http://(.*)", r"https://\1", url)
        
def test_check_valid_urls():
    valid_regex = "^https://(.*?)\.webstaurantstore\.com/(.*?)\.html(\?(.*?))?$"
    f = open("testUrls.txt", 'r')
    for line in f.readlines():
        line = line.strip()
        if re.match(NOT_GOOD, line):
            continue
        if re.match(valid_regex, line):
            print line

     
    f.close()

def test_beautiful_soup():
    f = urllib.urlopen("https://www.webstaurantstore.com")
    soup = BeautifulSoup(f.read())
    for link in soup.find_all('a'):
        print urlutils.formatUrl(link.get('href'))
    f.close()
    
def test_product_categories():
    links = webstaurantstoreUtils.get_base()
    for link in links:
        f = urllib.urlopen(link)
        soup = BeautifulSoup(f.read())
        for li in soup.find_all(class_='grid-item grid-parent'):
            #print li
            if li.name == 'span' and li.find('a'):
                print urlutils.formatUrl(li.a.get('href'))
                    
            elif li.name == 'a':
                print urlutils.formatUrl(li.get('href'))
        
        
            
def main():
#     testreplacehttps()
#     test_check_valid_urls()
#     test_beautiful_soup()
    test_product_categories()
    
if __name__ == '__main__':
    main()