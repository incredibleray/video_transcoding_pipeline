from absl import app, flags, logging
import json
import shlex
import subprocess
import base64
import re

FLAGS = flags.FLAGS

flags.DEFINE_string("source_video", None, "")
flags.DEFINE_boolean('debug_logs', False, '')
flags.DEFINE_boolean('remove_youtube_dl_filename_suffix', True, '')

def main(argv):
  if FLAGS.debug_logs:
    logging.set_verbosity(logging.DEBUG)

  if FLAGS.source_video is None:
    logging.fatal('no source video')
    return

  source_video_name=FLAGS.source_video
  if FLAGS.remove_youtube_dl_filename_suffix:
    suffix_pattern = re.compile('\d\d_\d\d_\d+(-[\w\d-]+)')
    suffix_string=suffix_pattern.findall(source_video_name)[0]
    
    youtube_dl_filename_suffix_start_index=source_video_name.rfind(suffix_string)
    source_video_name=source_video_name[:youtube_dl_filename_suffix_start_index]
  
  logging.debug('source video name is: %s', source_video_name)

  transcoded_video=base64.b64encode(source_video_name.encode('ascii')).decode('ascii')

  pass_1_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=640x360 -c:v libx264 -b:v 276k -g 1440 -threads 20 -preset veryslow -crf 36 -pass 1 -an -f null /dev/null
  '''

  pass_2_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=640x360 -c:v libx264 -b:v 276k -g 1440 -threads 20 -preset veryslow -crf 36 -pass 2 -c:a copy -pix_fmt yuv420p -movflags +faststart "transcoded_video/{transcoded_video}.mp4"
  '''

  generate_thumbnail_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4"  -ss 00:06:00 -vframes 1 "transcoded_video/{transcoded_video}.png"
  '''

  transcode_success=True
  for cmd_template in (pass_1_cmd_template, pass_2_cmd_template, generate_thumbnail_cmd_template,):
    cmd=cmd_template.format(
      source_video=FLAGS.source_video,
      transcoded_video=transcoded_video)

    args = shlex.split(cmd)
    logging.debug(args)

    p = subprocess.Popen(args)

    if p.wait() != 0:
      transcode_success=False
      break

  if transcode_success:
    logging.debug('source video %s transcoded to %s', FLAGS.source_video, transcoded_video)
  else:
    logging.debug('transcoding FAILED')

if __name__ == '__main__':
  app.run(main)
