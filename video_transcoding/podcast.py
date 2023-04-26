from absl import app, flags, logging
import json
import shlex
import subprocess
import base64
import re
import ffmpeg_command
from transcode_video import VideoTranscodeTask
import datetime
import requests
import xml.etree.ElementTree as ET
import uuid
import hashlib
from pydub import AudioSegment
import os

FLAGS = flags.FLAGS
flags.DEFINE_enum('lang', 
'en', 
['en', 'cn', 'kr', 'vi'], '')
flags.DEFINE_boolean('updateRss', False, '')

class Podcast():
  def __init__(self, source_video):
    self._source_video=source_video
    self._transcoded_video=None

  def Transcode(self):
    logging.debug(
      'source video is: %s', 
      self._source_video)

    source_video_name=self._source_video
    suffix_pattern = re.compile('(-[\w\d-]+)$')
    source_video_name=suffix_pattern.sub('', source_video_name)
    
    logging.debug(
      'cleaned source video name is: %s', 
      source_video_name)
    self._source_video_name=source_video_name

    
    dateStrPattern = re.compile('(\d+_\d+_\d+)')
    if dateStrPattern.findall(source_video_name):
      dateStr=dateStrPattern.findall(source_video_name)[0]
    else:
      dateStr=source_video_name.split(" ")[-1]

    hashStr = hashlib.sha256(source_video_name.encode()).hexdigest()[:6]
    transcoded_video=hashStr+"-"+dateStr
    
    if FLAGS.lang=="en":
      storageDir="podcast/EN"
    elif FLAGS.lang=="kr":
      storageDir="podcast/KR"
    else:
      transcoded_video=source_video_name
      storageDir="podcast/CN"

    self._transcoded_video=transcoded_video
    logging.debug(
      'transcoded video is: %s', 
      transcoded_video)

    cmds=[
"ffmpeg -y -i \"src_video/{source_video}.mp4\" -vn -c:a libmp3lame -q:a 0 \"transcoded_video/{transcoded_video}.mp3\" ",
"az storage azcopy blob upload -c \""+storageDir+"\" --account-name americanmahayana -s \"transcoded_video/{transcoded_video}.mp3\" "      
      ]

    # if FLAGS.lang in ("kr", "en"):
    # if FLAGS.lang =="kr":
    #   cmds=cmds[:1]
    
    podcast=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      cmds,
      )
    

    if podcast.Run():
      self._storagePath=storageDir+"/"+transcoded_video+".mp3"
      return True

    return False


class UpdateRss():
  def __init__(self, newEpisodes):
    self._newEpisodes=newEpisodes

  def Transcode(self):
    baseUrl="https://americanmahayana.blob.core.windows.net/"

    if FLAGS.lang=="en":
      rssFileName="podcast"
      storageDir="podcast"
    elif FLAGS.lang=="cn":
      rssFileName="podcastCN"
      storageDir="podcast/CN"
    elif FLAGS.lang=="kr":
      rssFileName="podcastKR"
      storageDir="podcast/KR"
    else:
      return False

    url=baseUrl+storageDir+"/"+rssFileName+".rss"
    rssFileReq = requests.get(url)

    if rssFileReq.ok==False:
      return False
      
    originalRssFile=open(rssFileName+".rss", "wb")
    originalRssFile.write(rssFileReq.content)
    originalRssFile.close()
    
    rssFile=open("transcoded_video/"+rssFileName+".rss", "w")
    
    for line in rssFileReq.text.split("\n"):
      if line.count("</channel>")>0:         
        for e in self._newEpisodes:
          newItem = ET.Element('item')
          nameElem=ET.SubElement(newItem, "title")
          nameElem.text=e['title']
          episodeType=ET.SubElement(newItem, "itunes:episodeType")
          episodeType.text="full"
          season=ET.SubElement(newItem, "itunes:season")
          season.text="2023"
          desc=ET.SubElement(newItem, 'description')
          desc.text=" "
          link=ET.SubElement(newItem, "link")
          if FLAGS.lang=="en":
            link.text="https://www.youtube.com/c/MasterYongHua"
          else:
            link.text=" "

          audioPath="transcoded_video/"+e['enclosure'].split("/")[-1]
          byteSize = os.path.getsize(audioPath)
          enclosure=ET.SubElement(newItem, "enclosure", {"type":"audio/mpeg", "url":e['enclosure'], 
          # "length":str(byteSize)
          })
          # guid=ET.SubElement(newItem, "guid")
          # guid.text=str(uuid.uuid4())
          pubDate=ET.SubElement(newItem, "pubDate")
          
          dateStrPattern = re.compile('(\d+)_(\d+)_(\d+)')
          if dateStrPattern.findall(e['title']):
            dateStr=dateStrPattern.findall(e['title'])[0]
            d=datetime.date(int(dateStr[0]), int(dateStr[1]), int(dateStr[2]))
          else:
            dateStr=e['title'].split(' ')[-1]
            d=datetime.date(int(dateStr[0:4]), int(dateStr[4:6]), int(dateStr[6:]))

          pubDate.text=d.strftime("%a, %d %b %Y")+"  19:20:00 -0700"

          duration=ET.SubElement(newItem, "itunes:duration")
          # Load the audio file
          audio = AudioSegment.from_file(audioPath, format="mp3")

          # Get the length of the audio in milliseconds
          length = len(audio)

          # Convert the length to minutes and seconds
          minutes = int(length / 1000 / 60)
          seconds = int(length / 1000 % 60)
          
          duration.text="{}:{:02d}".format(minutes,seconds)
          
          explicit=ET.SubElement(newItem, "itunes:explicit")
          explicit.text="false"

          rssStr=ET.tostring(newItem, encoding="unicode")
          rssFile.write(rssStr)
          rssFile.write("\n")
      rssFile.write(line+"\n")
    rssFile.flush()
    rssFile.close()

    podcast=VideoTranscodeTask(
      rssFileName, 
      "",
      [
"az storage azcopy blob upload -c \""+storageDir+"\" --account-name americanmahayana -s \"transcoded_video/{source_video}.rss\" "      
      ],
      )
    
    if FLAGS.updateRss is False:
      return True
    
    if podcast.Run():
      return True

    return False
