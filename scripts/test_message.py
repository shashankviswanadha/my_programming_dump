

#!/usr/bin/python

import urllib2
import cookielib
import sys

username = '8096640169'
passwd = 'waytohack'
#message = raw_input("Enter Message: ")
number = '8790191959'
"""message1 = "Chester)&1"
table = {'!':'(exclam)','@':'(at)','#':'(hash)','$':'(dollar)','%':'(mod)','&':'(and)','*': '(star)','(': '(open)',')':'(close)','_':'(under)'}
#message = "+".join(message.split(' '))
message = ''
for item in message1:
    if item in table:
        message = message + table[item]
    else:
        message = message + item
print message"""
for i in range(0,1):
    message = "Your fucking new zenphone is fucking hacked"
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

    #For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # Adding Header detail:
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]

    try:
        usock = opener.open(url, data)
    except IOError:
        pass
    #sys.exit(1)


    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
        print 'sent'
    except IOError:
        pass
        #sys.exit(1)
