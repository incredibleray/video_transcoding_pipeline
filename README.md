
# prepare video

## make a video path from the video title
```
echo "{video_title}" | base64
```

## make a thumbnail
```
ffmpeg -i "{video_path}.mp4"  -ss 00:06:00 -vframes 1 "{video_path}.png"
```

## h264 transcoding
[h264 encoding guide from ffmpeg](https://trac.ffmpeg.org/wiki/Encode/H.264)

```
ffmpeg -i "{input_video_path}.mp4" -vf 'format=yuv420p' -force_key_frames 'expr:gte(t,n_forced*5)' -c:v libx264 -preset slow -crf 22 -c:a copy -movflags +faststart "{output_video_path}.mp4"
```

To force insertion of keyframes, use `-force_key_frames 'expr:gte(t,n_forced*30)'` where the number is the interval of key frames, in this example, a key frame is inserted every 30 seconds.

### 2 pass h264 encoding
```
ffmpeg -y -i 'source.mp4' -c:v libx264 -b:v 1000k -preset veryslow -crf 29 -pass 1 -an -f null /dev/null && \
ffmpeg -y -i 'source.mp4' -vf 'format=yuv420p' -c:v libx264 -b:v 1000k -preset veryslow -crf 29 -pass 2 -c:a copy -movflags +faststart 'MjkpIE5vIEZpZ2h0aW5nLCBCZSBhIFN1cGVyaW9yIFBlcnNvbiAtIENoYW4gUWkgLSAwMS8yMy8yMDE4Cg==.mp4'
```

## vp9 transcoding
[vp9 encoding guide from ffmpeg](https://trac.ffmpeg.org/wiki/Encode/VP9)

```
ffmpeg -y -i 'source.mp4' -c:v libvpx-vp9 -b:v 1M -deadline best -pass 1 -an -f null /dev/null && \
ffmpeg -y -i 'source.mp4' -c:v libvpx-vp9 -b:v 1M -deadline best -pix_fmt yuv420p -pass 2 -c:a libopus 'MjkpIE5vIEZpZ2h0aW5nLCBCZSBhIFN1cGVyaW9yIFBlcnNvbiAtIENoYW4gUWkgLSAwMS8yMy8yMDE4Cg==.webm'
```