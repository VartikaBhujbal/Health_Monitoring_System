import urllib3

str_value = str(200)
url = "https://api.thingspeak.com/update?api_key=YPIH5SAYWH4I9ALT&field1=%s" %(str_value)

req = urllib3.PoolManager()     # Request
res = req.request('Post',url)   # Responce
