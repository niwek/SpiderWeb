'''
Created on Nov 12, 2014

@author: KWL
'''

import sys
import urllib
import re
import urlutils
from bs4 import BeautifulSoup


URL_REGEX = r'(?:href)=\"(.*?)\"'
BASE_URL = 'https://www.webstaurantstore.com'

def url_content(url_string):
    f = urllib.urlopen(url_string)
    contents = f.readlines()
    for content in contents:
        print content.strip()

def get_all_links(next_url, lst_urls, read_urls):
    try:
        f = urllib.urlopen(next_url)
    except IOError:
        print "Error: " + next_url
        return
    
    soup = BeautifulSoup(f.read())
    for link in soup.find_all('a'):   
        if link.get('href'):
            this_url =  urlutils.formatUrl(link.get('href'))
        else: continue
        if urlutils.check_valid(this_url) and this_url not in lst_urls and this_url not in read_urls:
            print this_url

            lst_urls.append(this_url)


    f.close()

def search(base_url):
    lst_urls = [base_url]
    read_urls = []

    
    while lst_urls:
        next_url = lst_urls.pop()
        read_urls.append(next_url)
        print "Urls that still need to be checked: " + str(len(lst_urls))
        print "Urls read so far: " + str(len(read_urls))
        contents = f.readlines()
        for content in contents:
            content = content.strip()
            result = re.search(URL_REGEX, content)
            this_url = ""
            if result:
                this_url = urlutils.formatUrl(result.group(1))
                 
                if urlutils.check_valid(this_url) and this_url not in lst_urls and this_url not in read_urls:
                    print this_url
                    lst_urls.append(this_url)
def main():
    '''
    Main function();
    '''
    search(BASE_URL)

if __name__ == "__main__":
    sys.exit(main())