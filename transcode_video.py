from absl import app, flags, logging
import json
import shlex
import subprocess
import base64
import re
import ffmpeg_command

FLAGS = flags.FLAGS

flags.DEFINE_boolean('remove_youtube_dl_filename_suffix', False, '')
flags.DEFINE_boolean('keep_source_video_filename', False, '')

class VideoTranscodeTask():
  def __init__(self, 
  source_video, 
  transcoded_video,
  cmd_templates,
  ):
    self._source_video=source_video
    self._transcoded_video=transcoded_video
    self._cmd_templates=cmd_templates

  def Run(self):
    for cmd_template in self._cmd_templates:
      cmd=cmd_template.format(
        source_video=self._source_video,
        transcoded_video=self._transcoded_video)

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
    if FLAGS.remove_youtube_dl_filename_suffix:
      suffix_pattern = re.compile('\d\d_\d\d_\d+(-[\w\d-]+)')
      suffix_string=suffix_pattern.findall(source_video_name)[0]
      
      youtube_dl_filename_suffix_start_index=source_video_name.rfind(suffix_string)
      source_video_name=source_video_name[:youtube_dl_filename_suffix_start_index]
    
    logging.debug(
      'cleaned source video name is: %s', 
      source_video_name)

    if FLAGS.keep_source_video_filename:
      transcoded_video=source_video_name
    else:
      transcoded_video=base64.b64encode(source_video_name.encode('ascii')).decode('ascii')

    self._transcoded_video=transcoded_video
    logging.debug(
      'transcoded video is: %s', 
      transcoded_video)

    h264_240p_transcode_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
        ffmpeg_command.h264_240p_pass_1_cmd_template,
        ffmpeg_command.h264_240p_pass_2_cmd_template,
      ]
      )
    h264_360p_transcode_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
        ffmpeg_command.h264_360p_pass_1_cmd_template,
        ffmpeg_command.h264_360p_pass_2_cmd_template,
      ]
      )
    h264_720p_transcode_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
        ffmpeg_command.h264_720p_pass_1_cmd_template,
        ffmpeg_command.h264_720p_pass_2_cmd_template,
      ]
      )
    generate_thumbnail_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
        ffmpeg_command.generate_thumbnail_cmd_template,
      ]
      )
    vp9_360p_transcode_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
      ffmpeg_command.vp9_360p_pass_1_cmd_template,
      ffmpeg_command.vp9_360p_pass_2_cmd_template,
      ]
      )

    if vp9_360p_transcode_task.Run() == False:
      return False

    return True
