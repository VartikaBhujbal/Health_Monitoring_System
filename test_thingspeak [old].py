
import urllib2
import time

baseURL='https://api.thingspeak.com/update?api_key=YPIH5SAYWH4I9ALT'
while True:
        c=c+2
        e=e-1
        d=str(c)
        g=str(e)

        try:
            print d
            print g
            f=urllib2.urlopen(baseURL + "&field1=%s&field2=%s&field3=%s" %(t,h,o))
            f.close()
            sleep(5)
        except:
            print 'exiting........'
