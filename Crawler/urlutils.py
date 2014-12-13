'''
Created on Nov 16, 2014

@author: KWL
'''

import re
import urllib


def check_valid(url):
    '''
    Checks if the url is a html page (not .jpg nor .png etc) and is part of the 'webstaurantstore.com'
    '''
    valid_regex = "^https://www\.webstaurantstore\.com/(.*?)\.html(\?page(.*?))?$"
    filter_regex = '(\?filter=|\?vendor=|\?withinval=)'
    return re.match(valid_regex, url) and not re.search(filter_regex, url)

def formatUrl(url):
    '''
    Format the url to have '^https://(.*?)$' in the beginning:
    
    
    '''
    base_url = 'https://www.webstaurantstore.com'
    if url.startswith("//"):
        formatted_url = "https:" + url
    elif url.startswith("/"):
        formatted_url = base_url + url
    elif url.startswith("http://"):
        formatted_url = re.sub(r"http://(.*)", r"https://\1", url)
    else:
        formatted_url = url
    return formatted_url