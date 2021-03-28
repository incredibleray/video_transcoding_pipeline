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
flags.DEFINE_string('source_audio', None, '')
flags.DEFINE_integer('threads', 16, '')

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
        source_audio=self._source_audio,
        threads=FLAGS.threads)

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
      suffix_pattern = re.compile('(-[\w\d-]+)$')
      source_video_name=suffix_pattern.sub('', source_video_name)
    
    logging.debug(
      'cleaned source video name is: %s', 
      source_video_name)
    self._source_video_name=source_video_name
    
    if FLAGS.keep_source_video_filename:
      transcoded_video=source_video_name
    else:
      transcoded_video=base64.b64encode(source_video_name.encode('utf-8')).decode('ascii')

    self._transcoded_video=transcoded_video
    logging.debug(
      'transcoded video is: %s', 
      transcoded_video)

    source_audio=''
    if FLAGS.source_audio is not None:
      source_audio='-i "src_video/{}.m4a"'.format(FLAGS.source_audio)

    h264_240p_transcode_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
        ffmpeg_command.h264_240p_pass_1_cmd_template,
        ffmpeg_command.h264_240p_pass_2_cmd_template,
      ],
      source_audio
      )
    h264_360p_transcode_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
        ffmpeg_command.h264_360p_pass_1_cmd_template,
        ffmpeg_command.h264_360p_pass_2_cmd_template,
      ],
      source_audio
      )
    h264_720p_transcode_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
        ffmpeg_command.h264_720p_pass_1_cmd_template,
        ffmpeg_command.h264_720p_pass_2_cmd_template,
      ],
      source_audio
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
      ],
      source_audio
      )
    extract_audio_task=VideoTranscodeTask(
      self._source_video, 
      transcoded_video,
      [
      ffmpeg_command.extract_soundtrack_template,
      
      ],
      )
    
    extract_audio_task.Run()
    # if generate_thumbnail_task.Run() == False:
    #   return False

    # if h264_240p_transcode_task.Run() == False:
    #   return False

    # if h264_360p_transcode_task.Run() == False:
    #   return False

    # if h264_720p_transcode_task.Run() == False:
    #   return False

    # if vp9_360p_transcode_task.Run() == False:
    #   return False

    return True
