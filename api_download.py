# -*- coding: utf-8 -*-

import requests

r=requests.get('http://api.dulun1918.com/1.0/audios/view/1769')

r.json()['rename']

li=[]

for i in range(1697, 1804):
  r=requests.get('http://api.dulun1918.com/1.0/audios/view/'+str(i))
  url='https://audio.dulun1918.com/'+r.json()['rename']
  li.append(url)

import json
json.dumps(li)