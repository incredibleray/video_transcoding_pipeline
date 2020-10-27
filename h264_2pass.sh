ffmpeg -y -i "src_video/${VIDEO_NAME}.mp4" -vf scale=640x480 -c:v libx264 -b:v 512k -g 240 -threads 20 -preset veryslow -crf 34 -pass 1 -an -f null /dev/null && \
ffmpeg -y -i "src_video/${VIDEO_NAME}.mp4" -vf scale=640x480 -c:v libx264 -b:v 512k -g 240 -threads 20 -preset veryslow -crf 34 -pass 2 -c:a copy -pix_fmt yuv420p -movflags +faststart "transcoded_video/${VIDEO_NAME}.mp4"
