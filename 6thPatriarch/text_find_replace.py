import shlex
import subprocess
from absl import app, flags, logging


FLAGS = flags.FLAGS

flags.DEFINE_string('sedFile', "transcript", '')
flags.DEFINE_string('textFile', None, '')

def main(argv):
  outFile="out.txt"
      
  sed_replace_template='''
    sed -f '{script}.sed' "{textFile}"
  '''

  cmd=sed_replace_template.format(
          script=FLAGS.sedFile,
          textFile=FLAGS.textFile,
          )

  args = shlex.split(cmd)
  logging.debug(args)

  with open(outFile, "w") as output_file:
    p = subprocess.Popen(args, stdout=output_file)

    if p.wait() != 0:
      logging.debug('text find replace FAILED')
      return False

    logging.debug(
        'output text is: %s', outFile)

    return True

if __name__ == '__main__':
  app.run(main)