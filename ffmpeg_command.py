generate_thumbnail_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4"  -ss 00:06:00 -vframes 1 "transcoded_video/{transcoded_video}.png"
  '''

h264_good_quality_pass_1_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=640x360 -c:v libx264 -b:v 276k -g 1440 -threads 20 -preset veryslow -crf 36 -pass 1 -an -f null /dev/null
  '''

h264_good_quality_pass_2_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=640x360 -c:v libx264 -b:v 276k -g 1440 -threads 20 -preset veryslow -crf 36 -pass 2 -c:a copy -pix_fmt yuv420p -movflags +faststart "transcoded_video/{transcoded_video}.mp4"
  '''

vp9_360p_good_quality_pass_1_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=640x360 -c:v libvpx-vp9 -b:v 276k -tile-columns 1 -g 1440 -threads 16 -quality good -speed 0 -crf 36 -pass 1 -an -f null /dev/null
'''

vp9_360p_good_quality_pass_2_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=640x360 -c:v libvpx-vp9 -b:v 276k -tile-columns 1 -g 1440 -threads 16 -quality good -speed 0 -crf 36 -pass 2 -c:a libopus -b:a 128k "transcoded_video/{transcoded_video}.webm"
'''

vp9_360p_low_quality_pass_1_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=640x360 -c:v libvpx-vp9 -b:v 150k -tile-columns 2 -g 1440 -threads 16 -quality best -speed 0 -crf 41 -pass 1 -an -f null /dev/null
'''

vp9_360p_low_quality_pass_2_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=640x360 -c:v libvpx-vp9 -b:v 150k -tile-columns 2 -g 1440 -threads 16 -quality best -speed 0 -crf 41 -pass 2 -c:a libopus -b:a 96k "transcoded_video/{transcoded_video}.webm"
'''

vp9_240p_pass_1_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=320x240 -c:v libvpx-vp9 -b:v 150k -tile-columns 0 -g 1440 -threads 16 -quality good -speed 0 -crf 37 -pass 1 -an -f null /dev/null
'''

vp9_240p_pass_2_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=320x240 -c:v libvpx-vp9 -b:v 150k -tile-columns 0 -g 1440 -threads 16 -quality good -speed 0 -crf 37 -pass 2 -c:a libopus -b:a 96k "transcoded_video/{transcoded_video}.webm"
'''

# h264 240p not very useful because the bitrate is the same as vp9 360p.
h264_240p_pass_1_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=320x240 -c:v libx264 -b:v 150k -g 1440 -threads 20 -preset veryslow -crf 37 -pass 1 -an -f null /dev/null
  '''

h264_240p_pass_2_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=320x240 -c:v libx264 -b:v 150k -g 1440 -threads 20 -preset veryslow -crf 37 -pass 2 -c:a aac -b:a 96k -pix_fmt yuv420p -movflags +faststart "transcoded_video/{transcoded_video}.mp4"
  '''
