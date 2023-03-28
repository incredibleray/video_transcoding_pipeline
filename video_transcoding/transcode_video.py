from absl import app, flags, logging
import json
import shlex
import subprocess
import base64
import re
import ffmpeg_command
import hashlib

FLAGS = flags.FLAGS

flags.DEFINE_boolean('dharmaGlimpse', True, '')
flags.DEFINE_string('source_audio', None, '')

class VideoTranscodeTask():
  def __init__(self, 
  source_video,
  transcoded_video,
  cmd_templates,
  source_audio='',
  ):
    self._source_video=source_video
    self._source_audio=source_audio
    self._transcoded_video=transcoded_video
    self._cmd_templates=cmd_templates

  def Run(self):
    for cmd_template in self._cmd_templates:
      cmd=cmd_template.format(
        source_video=self._source_video,
        transcoded_video=self._transcoded_video,
        source_audio=self._source_audio)

      args = shlex.split(cmd)
      logging.debug(args)

      p = subprocess.Popen(args)

      if p.wait() != 0:
        logging.debug('transcoding FAILED')
        return False

    logging.debug(
      'source video %s transcoded to %s', 
      self._source_video, 
      self._transcoded_video)
    return True

class Video():
  def __init__(self, source_video):
    self._source_video=source_video
    self._transcoded_video=None

  def Transcode(self):
    logging.debug(
      'source video is: %s', 
      self._source_video)

    source_video_name=self._source_video
    logging.debug(
      'cleaned source video name is: %s', 
      source_video_name)
    self._source_video_name=source_video_name
    
    if FLAGS.dharmaGlimpse:
      transcoded_video="dharmaglimpse-"+hashlib.sha256(source_video_name.encode()).hexdigest()[:6]
    else:
      transcoded_video=source_video_name


    self._transcoded_video=transcoded_video
    logging.debug(
      'transcoded video is: %s', 
      transcoded_video)

    source_audio=''
    if FLAGS.source_audio is not None:
      source_audio='-i "src_video/{}.mp4"'.format(FLAGS.source_audio)

    h264_transcode_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
        "ffmpeg -y -i \"src_video/{source_video}.mp4\" -c:v libx264 -preset veryslow -crf 14 -c:a aac -b:a 192k -pix_fmt yuv420p -movflags +faststart \"transcoded_video/{transcoded_video}.mp4\"",
        'ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=246:138 -ss 10 -vframes 1 "transcoded_video/{transcoded_video}.png"',
        "az storage azcopy blob upload -c \"media\" --account-name bli -s \"transcoded_video/{transcoded_video}.*\" " 
      ],
      )

    if h264_transcode_task.Run() == False:
      return False

    self._cloudVideoPath="https://bli.blob.core.windows.net/media/"+self._transcoded_video+".mp4"
    self._cloudThumbnailPath="https://bli.blob.core.windows.net/media/"+self._transcoded_video+".png"

    return True



    # h264_240p_transcode_task=VideoTranscodeTask(
    #   self._source_video, 
    #   transcoded_video,
    #   [
    #     ffmpeg_command.h264_240p_pass_1_cmd_template,
    #     ffmpeg_command.h264_240p_pass_2_cmd_template,
    #   ],
    #   source_audio
    #   )
    # h264_360p_transcode_task=VideoTranscodeTask(
    #   self._source_video, 
    #   transcoded_video,
    #   [
    #     ffmpeg_command.h264_360p_pass_1_cmd_template,
    #     ffmpeg_command.h264_360p_pass_2_cmd_template,
    #   ],
    #   source_audio
    #   )
    # h264_720p_transcode_task=VideoTranscodeTask(
    #   self._source_video, 
    #   transcoded_video,
    #   [
    #     ffmpeg_command.h264_720p_pass_1_cmd_template,
    #     ffmpeg_command.h264_720p_pass_2_cmd_template,
    #   ],
    #   source_audio
    #   )
    # generate_thumbnail_task=VideoTranscodeTask(
    #   self._source_video, 
    #   transcoded_video,
    #   [
    #     ffmpeg_command.generate_thumbnail_cmd_template,
    #   ]
    #   )
    # vp9_360p_transcode_task=VideoTranscodeTask(
    #   self._source_video, 
    #   transcoded_video,
    #   [
    #   ffmpeg_command.vp9_360p_pass_1_cmd_template,
    #   ffmpeg_command.vp9_360p_pass_2_cmd_template,
    #   ],
    #   source_audio
    #   )
    # extract_audio_task=VideoTranscodeTask(
    #   self._source_video, 
    #   transcoded_video,
    #   [
    #   ffmpeg_command.extract_soundtrack_template,
      
    #   ],
    #   )
      
    # # extract_audio_task.Run()

    # # if generate_thumbnail_task.Run() == False:
    # #   return False

    # # if h264_240p_transcode_task.Run() == False:
    # #   return False

    # # if h264_360p_transcode_task.Run() == False:
    # #   return False

    # if h264_720p_transcode_task.Run() == False:
    #   return False

    # # if vp9_360p_transcode_task.Run() == False:
    # #   return False