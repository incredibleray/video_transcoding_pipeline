from absl import app, flags, logging
import json
import base64
import re
import ffmpeg_command
from transcode_video import VideoTranscodeTask

FLAGS = flags.FLAGS

class StaticVideo():
  def __init__(self, source_audio, coverFile):
    self._source_audio=source_audio
    self._static_video_with_audio=None
    self.coverFile=coverFile

  def Transcode(self):
    logging.debug(
      'source audio is: %s', 
      self._source_audio)

    self._source_video_name=self._source_audio  
    self._static_video_with_audio=self._source_audio
    self._transcoded_video=self._static_video_with_audio
    
    logging.debug(
      'transcoded video is: %s', 
      self._static_video_with_audio)

    h264_generate_static_video_from_audio_task=VideoTranscodeTask(
      self._source_audio, 
      self._static_video_with_audio,
      [
        # '''
        # ffmpeg -y -f lavfi -i color=size=1280x720:rate=25:color=black -i 'src_video/{source_audio}.jpg' -i 'src_video/{source_video}.mp3' -filter_complex "[1:v]scale=1280:720" -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 128k -pix_fmt yuv420p -movflags +faststart -shortest 'transcoded_video/{transcoded_video}.mp4'
        # '''
        '''
        ffmpeg -y -loop 1 -framerate 24 -i 'src_video/{source_audio}.jpg' -i 'src_video/{source_video}.mp3'  -filter_complex "[0:v]scale=1280:720" -threads 7 -c:v libx264 -preset medium -tune stillimage -crf 18 -c:a copy -shortest -pix_fmt yuv420p -movflags +faststart 'transcoded_video/{transcoded_video}.mp4'  
        '''
      ],
      self.coverFile
      )

    if h264_generate_static_video_from_audio_task.Run() == False:
      return False

    return True
