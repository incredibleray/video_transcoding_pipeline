from absl import app, flags, logging
import json
import os
from transcode_video import Video
from audio_to_static_video import StaticVideo
from datetime import date

FLAGS = flags.FLAGS

flags.DEFINE_enum('operation', 'transcode_videos', ['transcode_videos', 'convert_audio_to_static_videos'], '')
flags.DEFINE_boolean('scan_dir_for_source_av_files', False, '')
flags.DEFINE_multi_string("source_video", None, "")
flags.DEFINE_boolean('debug_logs', False, '')
flags.DEFINE_string('write_to_manifest', None, '')

def transcode_videos(source_videos):
  manifest=[]
  for source_video in source_videos:
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

  return manifest

def convert_audio_to_static_videos(source_audios):
  manifest=[]
  for source_audio in source_audios:
    video=StaticVideo(source_audio)
    if video.Transcode():
      manifest_entry={
        'title': video._source_video_name,
        'chinese_title': '',
        'hash': '',
        'path': video._transcoded_video,
        'related_videos': [],
        'h264_streams':['240p', '360p', '720p'],
        "tags": [],
    "playlist": "chan_meditation",
    "date": date.today().isoformat(),
        }
      manifest.append(manifest_entry)

  return manifest

def main(argv):
  if FLAGS.debug_logs:
    logging.set_verbosity(logging.DEBUG)

  av_files=[]
  if FLAGS.scan_dir_for_source_av_files:
    for dir_entry in os.scandir('./src_video'):
      if dir_entry.is_file() and dir_entry.name.endswith('.mp3')==True:
        file_name, _=os.path.splitext(dir_entry.name)
        av_files.append(file_name)
  
  if FLAGS.source_video is not None:
    av_files=FLAGS.source_video

  if av_files == []:
    logging.fatal('no source av files')
    return

  if FLAGS.operation == 'transcode_videos':
    manifest=transcode_videos(av_files)
  
  if FLAGS.operation =='convert_audio_to_static_videos':
    manifest=convert_audio_to_static_videos(av_files)

  if FLAGS.write_to_manifest:
    manifest_file=open(FLAGS.write_to_manifest, 'w', encoding='utf-8')
    json.dump(manifest, manifest_file)

  

if __name__ == '__main__':
  app.run(main)
