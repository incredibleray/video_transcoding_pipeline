# -*- coding: utf-8 -*-
import os
from absl import logging

i=1

for dir_entry in os.scandir('./src_video'):
  if dir_entry.is_file() and dir_entry.name.endswith('.mp3')==True:
    file_name, _=os.path.splitext(dir_entry.name)
    target_file_name='./src_video/Bài số '+str(i)+'.mp3'
    

    logging.warning("renaming %s to %s", dir_entry.path, target_file_name)

    os.rename(dir_entry.path,target_file_name)

    i+=1
