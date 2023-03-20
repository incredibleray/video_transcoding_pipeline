from absl import app, flags, logging
import json
import os
from transcode_video import Video
from audio_to_static_video import StaticVideo
from text_find_replace import TextFindReplace
from datetime import date
from podcast import Podcast, UpdateRss

FLAGS = flags.FLAGS

flags.DEFINE_enum('operation', 
'podcast', 
['transcode_videos', 'convert_audio_to_static_videos', 'text_find_replace',
'podcast'], '')
flags.DEFINE_boolean('scan_dir_for_source_av_files', True, '')
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
        'url': video._cloudVideoPath,
        'thumbnail': video._cloudThumbnailPath,
        }
      manifest.append(manifest_entry)

  return manifest

def convert_audio_to_static_videos(source_audios):
  manifest=[]
  i=45
  for source_audio in source_audios:
    coverFile=str.format("KinhKimCang-{:02d}", i)
    video=StaticVideo(source_audio, coverFile)
    if video.Transcode():
      manifest_entry={
        'title': video._source_video_name,
        'chinese_title': '',
        'hash': '',
        'path': video._cloudPath,
        'related_videos': [],
        'h264_streams':['240p', '360p', '720p'],
        "tags": [],
    "playlist": "chan_meditation",
    "date": date.today().isoformat(),
        }
      manifest.append(manifest_entry)
      i+=1

  return manifest

def find_replace_texts(input_texts):
  for input_text in input_texts:
    video=TextFindReplace(input_text)
    video.Transcode()

  return []
  
def convert_videos_to_podcast(source_audios):
  manifest=[]
  for source_audio in source_audios:
    video=Podcast(source_audio)
    if video.Transcode():
      manifest_entry={
        'title': source_audio,
        "enclosure": "https://americanmahayana.blob.core.windows.net/"+video._storagePath,
        "fileName": video._transcoded_video+".mp3"
      }
      manifest.append(manifest_entry)

  # manifest=[{
  #       'title': "59) Chan Qi • One Hundred Days of Chan (193) - 20230102",
  #       "enclosure": "https://americanmahayana.blob.core.windows.net/podcast/EN/ChanQi20230102.mp3"
  #     }]
  uploadRss=UpdateRss(manifest)
  uploadRss.Transcode()

  return manifest

# def 
def main(argv):
  if FLAGS.debug_logs:
    logging.set_verbosity(logging.DEBUG)

  av_files=[]
  if FLAGS.scan_dir_for_source_av_files:
    if FLAGS.operation == 'transcode_videos':
      av_files_extension='.mp4'
  
    if FLAGS.operation =='convert_audio_to_static_videos':
      av_files_extension='.mp3'
      # av_files_extension='.m4a'

    if FLAGS.operation =='text_find_replace':
      av_files_extension='.txt'

    if FLAGS.operation == 'podcast':
      av_files_extension='.mp4'

    for dir_entry in os.scandir('./src_video'):
      if dir_entry.is_file() and dir_entry.name.endswith(av_files_extension)==True:
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

  if FLAGS.operation =='text_find_replace':
    manifest=find_replace_texts(av_files)

  if FLAGS.operation == 'podcast':
    manifest=convert_videos_to_podcast(av_files)

  if FLAGS.write_to_manifest:
    manifest_file=open(FLAGS.write_to_manifest, 'w', encoding='utf-8')
    json.dump(manifest, manifest_file)
  else:
    print(manifest)

  

if __name__ == '__main__':
  app.run(main)
