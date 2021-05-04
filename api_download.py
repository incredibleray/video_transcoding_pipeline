# -*- coding: utf-8 -*-

import requests

# r=requests.get('http://api.dulun1918.com/1.0/audios/view/1769')

# r.json()['rename']

for i in range(1697, 1804):
  r=requests.get('http://api.dulun1918.com/1.0/audios/view/'+str(i))
  audio=r.json()
  url='https://audio.dulun1918.com/'+audio['rename']

  talk = requests.get(url)

  name='transcoded_video/'+audio['name']+'.mp3'
  with open(name, 'wb') as f:
    f.write(talk.content)
