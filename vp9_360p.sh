ffmpeg -y -i "src_video/${VIDEO_NAME}.mp4" -vf scale=640x360 -c:v libvpx-vp9 -b:v 276k -tile-columns 1 -g 1440 -threads 2 -quality best -speed 0 -crf 36 -pass 1 -an -f null /dev/null && \
ffmpeg -y -i "src_video/${VIDEO_NAME}.mp4" -vf scale=640x360 -c:v libvpx-vp9 -b:v 276k -tile-columns 1 -g 1440 -threads 2 -quality best -speed 0 -crf 36 -pass 2 -c:a libopus "transcoded_video/${VIDEO_NAME}.webm"
