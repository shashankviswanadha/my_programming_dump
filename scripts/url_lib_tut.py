# -*- coding: utf-8 -*-
import urllib
import urllib2
"""x = urllib.urlopen('https://www.google.com')
url = 'http://pythonprogramming.net'
values = {'s': 'basic','submit':'search'}
data = urllib.urlencode(values)
data = data.encode('utf-8')
req = urllib2.Request(url,data)
resp = urllib2.urlopen(req)
respData = resp.read()
print respData"""
try:
    x = urllib.urlopen('https://www.google.com/search?selena')
    data = x.read()
    saveFile = open('withHeaders.html','w')
    saveFile.write(data)
    saveFile.close()
except Exception as e:
    print str(e)

"""try:
    url = 'https://www.google.com/search?q=test'
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    respData = resp.read()
    saveFile = open('withHeaders.html','w')
    saveFile.write(respData)
    saveFile.close()
except Exception as e:
    print str(e)"""
