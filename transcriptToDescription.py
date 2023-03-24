


from absl import app, flags, logging
import json
import os
import webvtt
from datetime import time

FLAGS = flags.FLAGS

flags.DEFINE_string('transcript', None, '')


desc='''00:00 | 🙏 Emitofuo 
01:20 | Requesting the Dharma
10:38 | Introduction
13:56 | Slide #03
14:49 | Malcolm's in Korea
15:34 | Slide #03
17:50 | Slide #04
22:44 | Slide #05
23:13 | Slide #06
25:46 | Slide #07
29:07 | Slide #08
30:27 | Q&A: Did Bodhidharma walk on foot from India to China?
32:38 | Q&A: Where did Bodhidharma went to in Vietnam? 
32:59 | Q&A: Did Bodhidharma come to China on a leaf?
37:38 | Q&A: What is the meaning behind Venerable Bodhidharma leaving on a leaf?
38:51 | Slide #08 The Sudden Teaching
40:43 | Slide #09
43:49 | Slide #10
44:59 | Slide #11
49:18 | Q&A: Is it possible that the 6th patriarch is a reincarnation of Shakyamuni Buddha?
56:17 | Slide #13
1:00:03 | Slide #14
1:01:04 | Slide #15
1:03:46 | Slide #16
1:05:55 | Anthony: Pronunciation of Nagarjuna.
1:06:32 | Slide #16-18
1:08:27 | Slide #19
1:12:26 | Slide #20
1:13:24 | Slide #21
1:16:42 | Slide #22
1:18:13 | Slide #23
1:20:41 | Slide #24
1:23:42 | Slide #25
1:25:04 | Slide #26
1:26:20 | Slide #27
1:26:47 | Slide #28
1:29:11 | Slide #29
1:36:20 | Slide #30
1:37:14 | Malcom: Bird impersonation
1:38:14 | Slide #31
1:39:17 | Slide #35
1:39:36 | Slide #36
1:43:10 | Slide #40
1:43:25 | Slide #41
1:44:52 | Slide #42
1:48:17 | Discussion: What language does Venerable Bodhidharma and Venerable ShenGuang use to communicate?
2:06:58 | Slide #43
2:07:45 | Discussion: How does Venerable Bodhidharma taught Venerable ShenGuang?
2:14:50 | Slide #43
2:17:37 | Slide #44
2:18:25 | Lecture ended on page 44'''

def main(argv):
    transcript=webvtt.from_srt(FLAGS.transcript)

    segments=[]

    for l in desc.split("\n"):
        timestampText=l.split("|")[0].strip()
        if len(timestampText.split(":"))==2:
            timestampText="00:"+timestampText
        else:
            timestampText="0"+timestampText

        t=time.fromisoformat(timestampText)
        segments.append([t,""])
        # print(t)

    i=0
    for caption in transcript:
        t=time.fromisoformat(caption.start)
        while i+1<len(segments) and t>=segments[i+1][0]:
            i+=1
        
        # print(caption, "is inserted to ", segments[i])
        segments[i][1]=segments[i][1]+" "+caption.text

    f=open("desc.html", "w", encoding="utf-8")
    for seg in segments:
        l=seg[0].isoformat()+" |"+seg[1].replace("\n", " ")+"<br/>\n"
        f.write(l)

if __name__ == '__main__':
  app.run(main)