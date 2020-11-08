from absl import app, flags, logging
import json
import shlex
import subprocess
import base64
import re
import ffmpeg_command

FLAGS = flags.FLAGS

flags.DEFINE_string("source_video", None, "")
flags.DEFINE_boolean('debug_logs', False, '')
flags.DEFINE_boolean('remove_youtube_dl_filename_suffix', False, '')
flags.DEFINE_boolean('keep_source_video_filename', False, '')
flags.DEFINE_string('write_to_manifest', None, '')

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

  if FLAGS.keep_source_video_filename:
    transcoded_video=source_video_name
  else:
    transcoded_video=base64.b64encode(source_video_name.encode('ascii')).decode('ascii')

  transcode_success=True
  for cmd_template in (
    # ffmpeg_command.h264_240p_separate_audio_video_track_pass_1_cmd_template,
    # ffmpeg_command.h264_240p_separate_audio_video_track_pass_2_cmd_template,
    # ffmpeg_command.vp9_360p_separate_audio_video_track_pass_1_cmd_template,
    # ffmpeg_command.vp9_360p_separate_audio_video_track_pass_2_cmd_template,
    ffmpeg_command.vp9_360p_pass_1_cmd_template,
    ffmpeg_command.vp9_360p_pass_2_cmd_template,
    # ffmpeg_command.generate_thumbnail_cmd_template,
    ):
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

    if FLAGS.write_to_manifest:
      # manifest_file=open('videos.json', 'r', encoding='utf-8')
      # manifest=json.load(manifest_file)

      manifest_entry={
        'title': source_video_name,
        'chinese_title': '',
        'hash': '',
        'path': transcoded_video,
        'related_videos': [],
        }
      # manifest.append(manifest_entry)
      manifest=[manifest_entry,]
      manifest_file=open(FLAGS.write_to_manifest, 'w', encoding='utf-8')
      json.dump(manifest, manifest_file)
      
  else:
    logging.debug('transcoding FAILED')

if __name__ == '__main__':
  app.run(main)
