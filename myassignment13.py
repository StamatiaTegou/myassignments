from urllib.request import Request, urlopen
import json
import urllib.request

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data2 = data.decode()
js = json.loads(data2)
ra = (js['randomness'])



n = 2
split = [ra[i:i + n] for i in range(0, len(ra), n)]

for i in range(len(split)):

    split[i] = int(split[i], base=16)
    split[i] = split[i] % 80

new_list = []

j = 0
for i in range(0,len(split)):
    temp = 'true'
    t = 0
    if j > 0:
        while temp == 'true' and t < j:
            if split[i] == new_list[t]:
                temp = 'false'
            else:
                t = t + 1
    if temp == 'true':
        new_list.append(split[i])
        j = j + 1

url2 = 'https://api.opap.gr/draws/v3.0/1100/last-result-and-active'
response = urllib.request.urlopen(url2)
re = response.read()
data3 = re.decode()
js2 = json.loads(data3)
l1 = (js2['last'])

l2 = (l1['winningNumbers'])
l3 = (l2['list'])

total = 0
for i in range(0, len(l3)):
  for j in range(0, len(new_list)):
    if l3[i] == new_list[j]:
      total = total + 1
print("The total of numbers that would have won in KINO are:",total)