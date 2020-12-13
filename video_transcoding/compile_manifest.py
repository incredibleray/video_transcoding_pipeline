from absl import app, flags, logging
import json
import os

FLAGS = flags.FLAGS

flags.DEFINE_string("manifests_location", None, "")
flags.DEFINE_boolean('debug_logs', False, '')
flags.DEFINE_string('compiled_manifest_path', None, '')

def main(argv):
  if FLAGS.debug_logs:
    logging.set_verbosity(logging.DEBUG)

  if FLAGS.manifests_location is None:
    logging.fatal('no manifest location')
    return

  manifest=[]
  for manifest_file in os.scandir(FLAGS.manifests_location):
    manifest_file_reader=open(manifest_file.path, 'r', encoding='utf-8')
    entries=json.load(manifest_file_reader)

    manifest=manifest+entries

  if FLAGS.compiled_manifest_path:
    compiled_manifest_writer=open(FLAGS.compiled_manifest_path, 'w', encoding='utf-8')
    json.dump(manifest, compiled_manifest_writer)

if __name__ == '__main__':
  app.run(main)
