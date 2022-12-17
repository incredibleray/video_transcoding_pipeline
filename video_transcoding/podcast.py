from absl import app, flags, logging
import json
import shlex
import subprocess
import base64
import re
import ffmpeg_command
from transcode_video import VideoTranscodeTask
import datetime

FLAGS = flags.FLAGS
flags.DEFINE_enum('lang', 
'en', 
['en', 'cn', ], '')

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

    dateStr=source_video_name.split(" ")[-1]
    date=datetime.date(int(dateStr[:4]), int(dateStr[4:6]), int(dateStr[6:]))
    self._pubDate=date.strftime("%a, %d %b %Y")

    if FLAGS.lang=="en":
      transcoded_video="ChanQi"+dateStr
      storageDir="podcast/EN"
    else:
      transcoded_video=source_video_name
      storageDir="podcast/CN"

    self._transcoded_video=transcoded_video
    logging.debug(
      'transcoded video is: %s', 
      transcoded_video)


    podcast=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
"ffmpeg -y -i \"src_video/{source_video}.mp4\" -vn -c:a libmp3lame -q:a 0 \"transcoded_video/{transcoded_video}.mp3\" ",
"az storage azcopy blob upload -c \""+storageDir+"\" --account-name americanmahayana -s \"transcoded_video/{transcoded_video}.mp3\" "      
      ],
      )
    

    if podcast.Run():
      self._storagePath=storageDir+"/"+transcoded_video+".mp3"
      return True

    return False
