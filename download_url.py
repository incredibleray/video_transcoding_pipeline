import requests

urls=[
  "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A075_Ch01-4.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A131.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A132.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A133.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A134.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A135.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A136.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A137.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A138.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A139.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A140.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A141.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A142.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A208.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A252.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A256_Ch15.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A269.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A343.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A479.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A486.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A494.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A508.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A528.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A610.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A619.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A624.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A626.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A633.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A634.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A638.mp3",
 "http://dharmalib.org/Master-Hua-Chinese/Sutras-The-Flower-Adornment-Sutra/A677.mp3"
]
import time

for url in urls:
  if url.endswith('.m3u'):
    continue

  try:
    talk = requests.get(url)
    name='transcoded_video/'+url.split('/')[-1]
    with open(name, 'wb') as f:
      f.write(talk.content)

  except:
    print("", url)

  time.sleep(3)