ffmpeg -y -i "src_video/${VIDEO_NAME}.mp4" -vf scale=640x360 -c:v libx264 -b:v 276k -g 1440 -threads 20 -preset veryslow -crf 36 -pass 1 -an -f null /dev/null && \
ffmpeg -y -i "src_video/${VIDEO_NAME}.mp4" -vf scale=640x360 -c:v libx264 -b:v 276k -g 1440 -threads 20 -preset veryslow -crf 36 -pass 2 -c:a copy -pix_fmt yuv420p -movflags +faststart "transcoded_video/${VIDEO_NAME}.mp4"
