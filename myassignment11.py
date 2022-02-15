from urllib.request import Request, urlopen
import json
import urllib.request
import math


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data2 = data.decode()
js = json.loads(data2)
round1 = (js['round'])

round1= int(round1)
round1 = round1 - 1
round1 = str(round1)
x = ""
for i in range(1, 20):
    siteExtension = round1
    req = Request('https://drand.cloudflare.com/public/' + str(siteExtension),
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data11 = urlopen(req).read()
    data22 = data11.decode()
    js2 = json.loads(data22)
    round1 = (js2['round'])
    ran = (js2['randomness'])
    round1 = int(round1)
    round1 = round1 - 1
    round1 = str(round1)
    x = x + ran
x2 = int(x, base=16)
x2 = str(x2)

def entropy(x2):
    prob = [float(x2.count(c)) / len(x2) for c in dict.fromkeys(list(x2))]
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
    return entropy
print("The entropy of the text is:", entropy(x2))