from absl import logging
import shlex
import subprocess

sed_replace_template='''
  sed -f 'src_video/script.sed' "src_video/{source_video}.txt"
'''

class TextFindReplace():
  def __init__(self, input_text):
    self._input_text=input_text
    self._static_video_with_audio=None

  def Transcode(self):
    logging.debug(
      'input text is: %s', 
      self._input_text)

    self._output_text="transcoded_video/{}.txt".format(self._input_text)
    
    cmd=sed_replace_template.format(
        source_video=self._input_text,
        )

    args = shlex.split(cmd)
    logging.debug(args)

    with open(self._output_text, "w") as output_file:
      p = subprocess.Popen(args, stdout=output_file)

      if p.wait() != 0:
          logging.debug('text find replace FAILED')
          return False

    logging.debug(
      'output text is: %s', 
      self._output_text)

    return True
