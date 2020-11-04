
# prepare video

## make a video path from the video title
```
echo "{video_title}" | base64
```

## make a thumbnail
```
ffmpeg -i "{video_path}.mp4"  -ss 00:06:00 -vframes 1 "{video_path}.png"
```

[a good guide for h264, vp9 and ogg](https://www.s-config.com/video-transcoding-ffmpeg/)

[test video Big Buck Bunny](http://bbb3d.renderfarming.net/download.html)

## h264 transcoding

presets are in the `h264_2pass.sh` script, run 

```
VIDEO_NAME='...' ./h264_2pass.sh
```

to transcode.

[h264 encoding guide from ffmpeg](https://trac.ffmpeg.org/wiki/Encode/H.264)

[youtube video encoding guide](https://trac.ffmpeg.org/wiki/Encode/YouTube)

[rate control](https://slhck.info/video/2017/03/01/rate-control.html)

```
ffmpeg -y -i 'source.mp4' -c:v libx264 -b:v 1000k -preset veryslow -crf 29 -pass 1 -an -f null /dev/null && \
ffmpeg -y -i 'source.mp4' -vf 'format=yuv420p' -c:v libx264 -b:v 1000k -preset veryslow -crf 29 -pass 2 -c:a copy -movflags +faststart 'MjkpIE5vIEZpZ2h0aW5nLCBCZSBhIFN1cGVyaW9yIFBlcnNvbiAtIENoYW4gUWkgLSAwMS8yMy8yMDE4Cg==.mp4'
```


## vp9 transcoding
[vp9 encoding guide from ffmpeg](https://trac.ffmpeg.org/wiki/Encode/VP9)

[google media guide](https://developers.google.com/media/vp9/settings/vod/)

[google media encoding bitrate guide](https://developers.google.com/media/vp9/settings#encoding_bitrates)

```
ffmpeg -y -i 'source.mp4' -c:v libvpx-vp9 -b:v 1M -quality best -speed 0 -pass 1 -an -f null /dev/null && \
ffmpeg -y -i 'source.mp4' -c:v libvpx-vp9 -b:v 1M -quality best -speed 0 -pix_fmt yuv420p -pass 2 -c:a libopus 'MjkpIE5vIEZpZ2h0aW5nLCBCZSBhIFN1cGVyaW9yIFBlcnNvbiAtIENoYW4gUWkgLSAwMS8yMy8yMDE4Cg==.webm'
```

## ogg transcoding
[ogg ffmpeg](https://trac.ffmpeg.org/wiki/TheoraVorbisEncodingGuide)

```
ffmpeg -i "src_video/${VIDEO_NAME}.mp4" -vf scale=640x360 -codec:v libtheora -qscale:v 5 -codec:a libvorbis -qscale:a 3 "transcoded_video/${VIDEO_NAME}.ogv"
```

## ffprobe
[ffprobe tips](https://trac.ffmpeg.org/wiki/FFprobeTips)


`ffprobe -v error -show_format -show_streams input.mp4`

# CDN

## CDN purge
CDN content is cached, if there is an update of the content in storage container, the CDN content is **not** updated (can be stale for up to many days).

To force a sync on CDN, we need to purge the content that is on CDN. 

go to Azure CDN page, click purge, and put `container/${file_name}` in content, click purge.


# making debug/sample video

using Big Buck Bunny.

for some reason the original link has broken videos...

[original download link](http://bbb3d.renderfarming.net/download.html) 

[youtube link](https://www.youtube.com/watch?v=YE7VzlLtp-4)

truncating video:

```
ffmpeg -i big_buck_bunny.mp4 -t 00:03:44 -c copy debug_video.mp4
```