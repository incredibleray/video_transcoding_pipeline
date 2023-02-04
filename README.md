

# make a thumbnail
```
ffmpeg -i "{video_path}.mp4"  -ss 00:06:00 -vframes 1 "{video_path}.png"
```

[a good guide for h264, vp9 and ogg](https://www.s-config.com/video-transcoding-ffmpeg/)

[test video Big Buck Bunny](http://bbb3d.renderfarming.net/download.html)

# h264 transcoding

presets are in the `h264_2pass.sh` script, run 

```
VIDEO_NAME='...' ./h264_2pass.sh
```

to transcode.

[h264 encoding guide from ffmpeg](https://trac.ffmpeg.org/wiki/Encode/H.264)

[youtube video encoding guide](https://trac.ffmpeg.org/wiki/Encode/YouTube)

[rate control](https://slhck.info/video/2017/03/01/rate-control.html)


# vp9 transcoding
[vp9 encoding guide from ffmpeg](https://trac.ffmpeg.org/wiki/Encode/VP9)

[google media guide](https://developers.google.com/media/vp9/settings/vod/)

[google media encoding bitrate guide](https://developers.google.com/media/vp9/settings#encoding_bitrates)


# make a static picture video from audio file
```
ffmpeg -y -f lavfi -i color=size=320x240:rate=1:color=black -i src_video/Symptom-\ Stress-\ Part\ 2-\ 20\ Min-\ Day\ 10.mp3 -vf "drawtext=fontfile=/System/Library/Fonts/NewYork.ttf: text='Stress Relief Part 2 Day 10': fontcolor=white: fontsize=24: x=(w-text_w)/2: y=(h-text_h)/2" -c:v libx264 -preset fast -crf 18 -c:a aac -b:a 128k -shortest -pix_fmt yuv420p -movflags +faststart transcoded_video/output.mp4
```

## picture + text

```
ffmpeg -y -f lavfi -i color=size=1280x720:rate=25:color=black -i cover.png -i audio.mp3 -filter_complex "[1:v]scale=1280:720 [ovrl], [0:v][ovrl]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2, drawtext=fontfile=/System/Library/Fonts/NewYork.ttf: text='Amitabha Sutra': fontcolor=black: fontsize=24: x=3*(w-text_w)/4: y=3*(h-text_h)/4" -c:v libx264 -preset slow -crf 18 -c:a aac -b:a 128k -t 00:01:00 -pix_fmt yuv420p -movflags +faststart output.mp4
```

# replace audio track in video
```
ffmpeg -i src_video.mp4 -i src_audio.m4a -map 0:v -map 1:a -c copy output.mp4
```

# extract audio from video
```
ffmpeg -i .mp4 -vn -c copy output.m4a

```

# concat audio
```
ffmpeg -f concat -safe 0 -i concat.txt -c copy 5hr_sleep.m4a
```

# dharma glimpse
```
ffmpeg -y -i src_video/dharma.mp4  -ss 00:46:43 -t 00:00:39 -c copy transcoded_video/dharma_glimpse.mp4

ffmpeg -y -i transcoded_video/dharma_glimpse.mp4 -i bodhilight.png -filter_complex "overlay=x=(main_w-overlay_w):y=(main_h-overlay_h)" transcoded_video/dharma_glimpse_watermark.mp4

ffmpeg -y -i src_video/dharma.mp4 -vf scale=-1:240 -ss 00:46:43  -vframes 1 "transcoded_video/dharma.png"

ffmpeg -i a.jpg -i b.jpg -filter_complex hstack output.jpg

47:22
```

# translation video
```

ffmpeg -y -i src_video/chnraw.mp4 -ss 00:01:00 -vn src_video/chn.m4a

ffmpeg -y -i chopin_concerto_1.m4a -af "adelay=10000|10000" test.m4a

ffmpeg -y -i src_video/eng.mp4 -i src_video/chn.m4a -filter_complex "[0:a]volume=0.5[a];[1:0]volume=4.0[b];[a][b]amix=inputs=2:duration=first" transcoded_video/chn.mp4 
```

## fix translation head
```
ffmpeg -y -i "recording.mp4" -ss 00:03 -vn -c copy  frontChn.m4a 

ffmpeg -y -i frontChn.m4a -i "en.mp4" -filter_complex "[0:0]volume=24.0[a];[1:a]volume=0.7[b];[a][b]amix=inputs=2:duration=first" -t 25:52 -vn frontMix.m4a

ffmpeg -y -i "cn.mp4" -ss 24:37 -vn -c copy backChn.m4a 

ffmpeg -y -i frontMix.m4a -i backChn.m4a -filter_complex "[0:a][1:a]concat=n=2:v=0:a=1" chn.m4a

ffmpeg -y -i "en.mp4" -i chn.m4a -map 0:v -map 1:a -c copy chn.mp4

```

## concat videos
```
ffmpeg -i mmbPlaque1.mp4 -i mmbPlaque2.mp4 -i mmbPlaque3.mp4 -filter_complex "[0:v:0][0:a:0][1:v:0][1:a:0][2:v:0][2:a:0]concat=n=3:v=1:a=1[outv][outa]" -map "[outv]" -map "[outa]" out1.mp4
```
