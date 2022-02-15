from urllib.request import Request, urlopen
import json
import urllib.request
import math


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data2 = data.decode()
js = json.loads(data2)
round1 = (js['round'])

round1 = int(round1)
round1 = round1 - 1
round1 = str(round1)
x = ""
for i in range(1, 2):
    siteExtension = round1
    req = Request('https://drand.cloudflare.com/public/' + str(siteExtension),
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data11 = urlopen(req).read()
    data22 = data11.decode()
    js2 = json.loads(data22)
    round1 = (js2['round'])
    ran = (js2['randomness'])
    ran2 = ''.join(format(ord(x), 'b') for x in ran)
    round1 = int(round1)
    round1 = round1 - 1
    round1 = str(round1)
    x = x + ran2
total0 = 0
total1 = 0
max0 = 0
max1 = 0
prevnu = ''
for element in x:
    if element == '1':
        if prevnu == '0':
            total0 = 0
        total1 = total1 + 1
        if total1 > max1:
          max1 = total1
        prevnu = '1'
    else:
       if prevnu == '1':
            total1 = 0
       total0 = total0 + 1
       if total0 > max0:
         max0 = total0
       prevnu = '0'

print("The max amount of the number is:",  max1, "The max amount of the number 0 is:", max0)
