extract_soundtrack_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" -vn -c:a libmp3lame -q:a 6 "transcoded_video/{transcoded_video}.mp3"
  '''


generate_thumbnail_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" -vf scale=-1:240 -ss 00:06:00 -vframes 1 "transcoded_video/{transcoded_video}.png"
  '''

h264_240p_pass_1_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=320x240 -c:v libx264 -b:v 150k -g 1440 -threads {threads} -preset veryslow -crf 37 -pass 1 -an -f null /dev/null
  '''

h264_240p_pass_2_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=320x240 -c:v libx264 -b:v 150k -g 1440 -threads {threads} -preset veryslow -crf 37 -pass 2 -c:a aac -b:a 96k -pix_fmt yuv420p -movflags +faststart "transcoded_video/{transcoded_video}.mp4"
  '''

vp9_360p_pass_1_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x360 -c:v libvpx-vp9 -b:v 130k -tile-columns 2 -g 1440 -threads {threads} -quality best -speed 0 -crf 41 -pass 1 -an -f null /dev/null
'''

vp9_360p_pass_2_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x360 -c:v libvpx-vp9 -b:v 130k -tile-columns 2 -g 1440 -threads {threads} -quality best -speed 0 -crf 41 -pass 2 -c:a libopus -b:a 128k "transcoded_video/{transcoded_video}.webm"
'''

# WIP
vp9_480p_pass_1_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x360 -c:v libvpx-vp9 -b:v 276k -tile-columns 1 -g 1440 -threads {threads} -quality good -speed 0 -crf 36 -pass 1 -an -f null /dev/null
'''

vp9_480p_pass_2_cmd_template='''
ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x360 -c:v libvpx-vp9 -b:v 276k -tile-columns 1 -g 1440 -threads {threads} -quality good -speed 0 -crf 36 -pass 2 -c:a libopus -b:a 128k "transcoded_video/{transcoded_video}.480p.webm"
'''

h264_360p_pass_1_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x360 -c:v libx264 -b:v 276k -g 1440 -threads {threads} -preset veryslow -crf 36 -pass 1 -an -f null /dev/null
  '''

h264_360p_pass_2_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x360 -c:v libx264 -b:v 276k -g 1440 -threads {threads} -preset veryslow -crf 36 -pass 2 -c:a copy -pix_fmt yuv420p -movflags +faststart "transcoded_video/{transcoded_video}.360p.mp4"
  '''

h264_480p_pass_1_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x480 -c:v libx264 -b:v 512k -g 1440 -threads {threads} -preset veryslow -crf 34 -pass 1 -an -f null /dev/null
  '''

h264_480p_pass_2_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x480 -c:v libx264 -b:v 512k -g 1440 -threads {threads} -preset veryslow -crf 34 -pass 2 -c:a copy -pix_fmt yuv420p -movflags +faststart "transcoded_video/{transcoded_video}.480p.mp4"
  '''

h264_720p_pass_1_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x480 -c:v libx264 -b:v 512k -g 1440 -threads {threads} -preset veryslow -crf 34 -pass 1 -an -f null /dev/null
  '''

h264_720p_pass_2_cmd_template='''
  ffmpeg -y -i "src_video/{source_video}.mp4" {source_audio} -vf scale=640x480 -c:v libx264 -b:v 512k -g 1440 -threads {threads} -preset veryslow -crf 34 -pass 2 -c:a copy -pix_fmt yuv420p -movflags +faststart "transcoded_video/{transcoded_video}.720p.mp4"
  '''

h264_generate_static_video_from_audio_cmd_template='''
ffmpeg -y -f lavfi -i color=size=1280x720:rate=25:color=black -i 'src_video/cover.png' -i 'src_video/{source_video}.mp3' -filter_complex "[1:v]scale=1280:720 [ovrl], [0:v][ovrl]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2, drawtext=fontfile=/Windows/Fonts/Arial.ttf: text='{source_video}': fontcolor=black: fontsize=24: x=0.90*(w-text_w): y=0.68*(h-text_h)" -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 128k -pix_fmt yuv420p -movflags +faststart -shortest 'transcoded_video/{transcoded_video}.mp4'
'''