'''
Created on Jan 19, 2014

@author: dirai
'''
import urllib.request
import sys
import re


def one():
    url = "http://www.google.com/"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    print (html)

    length = len(html)
    print (length)
    startIndex = 0
    endIndex = 0;
    while startIndex < length:
        startIndex= html.find('<')
        endIndex=html.find('>')
        if (startIndex == -1 or endIndex == -1):
            break
        tag = html[startIndex:endIndex+1]
        html=html.replace(tag," ")
        startIndex=endIndex+1
    print (html)
    
def two():
    url = "http://www.google.com/"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    print (html)

    length = len(html)
    print (length)
    
    
if __name__ == "__main__":
    if len(sys.argv) == 2:
        argument = sys.argv[1]
        if argument == "one":
            one()
        
    else:
        one()
'''
for line in html:
    startIndex = 0
    length = len(line)
    while startIndex < len( line )-1:
        startIndex = line.find('<')
        endIndex = line.find('>')
        if startIndex == -1 or endIndex == -1:
            break
        tag = line[startIndex:endIndex+1]
        print (line)
        line = line.replace(tag, " ")
        print (line)
        startIndex = endIndex+1
 '''   