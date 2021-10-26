from absl import app, flags, logging
import json
import base64
import re
import ffmpeg_command
from transcode_video import VideoTranscodeTask

FLAGS = flags.FLAGS

class StaticVideo():
  def __init__(self, source_audio):
    self._source_audio=source_audio
    self._static_video_with_audio=None

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

    source_audio=''

    h264_generate_static_video_from_audio_task=VideoTranscodeTask(
      self._source_audio, 
      self._static_video_with_audio,
      [
        ffmpeg_command.h264_generate_static_video_from_audio_cmd_template
      ],
      source_audio
      )

    mp3_bitrate_compression_and_volume_tuning_task=VideoTranscodeTask(
      self._source_audio, 
      self._transcoded_video,
      [
        ffmpeg_command.mp3_bitrate_compression_and_volume_tuning_template
      ],
      source_audio
      )

    # if h264_generate_static_video_from_audio_task.Run() == False:
    #   return False

    if mp3_bitrate_compression_and_volume_tuning_task.Run() == False:
      return False
      
    return True
