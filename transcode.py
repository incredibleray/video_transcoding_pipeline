from absl import app, flags, logging
import json
import shlex
import subprocess
import base64
import re
import ffmpeg_command
from transcode_video import Video

FLAGS = flags.FLAGS

flags.DEFINE_multi_string("source_video", None, "")
flags.DEFINE_boolean('debug_logs', False, '')
flags.DEFINE_string('write_to_manifest', None, '')

def main(argv):
  if FLAGS.debug_logs:
    logging.set_verbosity(logging.DEBUG)

  if FLAGS.source_video is None:
    logging.fatal('no source video')
    return

  manifest=[]
  for source_video in FLAGS.source_video:
    video=Video(source_video)
    if video.Transcode():
      manifest_entry={
        'title': video._source_video_name,
        'chinese_title': '',
        'hash': '',
        'path': video._transcoded_video,
        'related_videos': [],
        'h264_streams':['240p', '360p', '720p']
        }
      manifest.append(manifest_entry)

  if FLAGS.write_to_manifest:
    manifest_file=open(FLAGS.write_to_manifest, 'w', encoding='utf-8')
    json.dump(manifest, manifest_file)

if __name__ == '__main__':
  app.run(main)
