# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:00:39 2021

@author: Akash
"""


## Module urllib.urlrequest contains a function called 
## urlopen that opens a web page for reading. 
## urlopen returns a file-like object that you can use 
## much as if you were reading a local file.
        
import urllib.request
import urllib.parse
import io

def encode_url_demo():
    query = 'Hellö+Wörld @ Python🐍'
    # The quote() function by default uses UTF-8 encoding scheme.
    encoded_str = urllib.parse.quote(query)
    print("Encoded String :",encoded_str)
    # The quote() function encodes space characters to %20. If you want to encode space characters to plus sign (+), then you can use  quote_plus provided by urllib.parse package.
    encoded_str = urllib.parse.quote_plus(query)
    print("Encoded String :",encoded_str)

# Using urllib.urlopen() will return a response object, which can be handled similar to a file.

# Pass the URL to urlopen() to get a “file-like” handle to the remote data.
from urllib import request

def requestDemo(url):
    # on success return http.client.HTTPResponse
    response = request.urlopen(url)
    print(type(response))
    print('RESPONSE:', response)
    print('URL     :', response.geturl())
    print("Encoding :",response.encoding)
    headers = response.info()
    print('DATE    :', headers['date'])
    print('HEADERS :')
    print('---------')
    print(headers)
    
    data = response.read().decode('utf-8')
    print('LENGTH  :', len(data))
    print('DATA    :')
    print('---------')
    print(data)
    
    
def readWebPage(url):
# The file-like object returned by urlopen() is iterable:
    with request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            # print(type(line))
            line = line.decode('utf-8')
            print(line)

def saveWebPage(urlToRead, destFile):
    outFile = open(destFile,"wt")
    with request.urlopen(urlToRead) as webpage:
        for line in webpage:
            # line = line.strip()
            line = line.decode('utf-8')
            # print(line)
            outFile.write(str(line))
            outFile.write("</br>")
        
    # page = urllib.request.urlopen(url).read() #->byte String
    # page = 
    # outFile.write(page)
    outFile.close()
    
def passingParameters():
    # query_parms = {'username':'hrishipisal@gmail.com', 'password':'acd1234'}
    # encoded_parms=urllib.parse.urlencode(query_parms).encode('utf-8')
    # response = urllib.request.urlopen("https://stackoverflow.com/users/login", encoded_parms)
    
    url = "https://www.bing.com/search?"
    query_parms = {'query':'q=pune'}
    encoded_parms=urllib.parse.urlencode(query_parms).encode('utf-8')
    # url = url+encoded_parms.decode('utf-8')
    # print(url)
    url = url+encoded_parms
    print(url)
    response = urllib.request.urlopen(url)
    print("Response Code :",response.code)
    data = response.read()
    print(data)
    outFile = open("d:\\sai.html","w")
    outFile.write(str(data))
    outFile.close()
    text = io.TextIOWrapper(response)
    # print("***************************")
    # print(text.read())
    # print(data,file=open("d:/account.html","w"))



# The urllib.parse module provides functions for manipulating URLs and their component parts, to either break them down or build them up.
from urllib.parse import urlparse 

# Parsing
# The return value from the urlparse() function is a ParseResult object that acts like a tuple with six elements.
def url_parse_demo():
    url = 'http://netloc/path;param?query=arg#frag'
    url = 'https://www.bing.com/search?q=pune'
    parsed = urlparse(url) # ParseResult object as Tuple
    print("Details from ParseResult object")
    print(parsed)
   
    
if __name__ == '__main__':
    
     encode_url_demo()
     # url = 'http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
     # url ='https://hi.wikipedia.org/wiki/%E0%A5%A8%E0%A5%AF_%E0%A4%9C%E0%A4%A8%E0%A4%B5%E0%A4%B0%E0%A5%80'
     # url= 'https://en.wikipedia.org/wiki/Wiki'
     # url= 'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5'
     # requestDemo(url)
     # readWebPage(url)
     # url = "https://www.york.ac.uk/teaching/cws/wws/webpage2.html"
     # saveWebPage(url,"avinash.html")
     passingParameters()
     url_parse_demo()


    