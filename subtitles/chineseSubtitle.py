


from absl import app, flags, logging
import re
from datetime import time

FLAGS = flags.FLAGS

flags.DEFINE_string('transcript', None, '')

def main(argv):
    vietnamese_pattern = re.compile("[^\u0000-\u007F\u0102\u0103\u0110\u0111\u0128\u0129\u0168\u0169\u01A0\u01A1\u01AF\u01B0\u1EA0-\u1EF9]+")

    f=open("puxian.txt", "r", encoding="utf-8")
    out=open("universalWorthVowsChapter.txt", "w", encoding="utf-8")

    for l in f.readlines():
        if len(l)==0:
            continue
        
        filtered_text = vietnamese_pattern.sub("", l)
        out.write(filtered_text)
        # print(t)

    out.close()

if __name__ == '__main__':
  app.run(main)