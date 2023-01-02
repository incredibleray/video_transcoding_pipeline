


from absl import app, flags, logging
import json
import os
import webvtt
from datetime import time

FLAGS = flags.FLAGS

flags.DEFINE_string('transcript', None, '')


desc='''00:00:00 | 🙏 Emitofuo 
00:01:00 | Requesting the Dharma
00:04:29 | Invocations
00:07:34 | Date and Place
00:07:44 | Introduction
00:07:55 | Slide 45
00:12:40 | Slide 46
00:14:01 | Slide 47
00:16:22 | Slide 48
00:18:07 | Anthony Question: Why did Bodhidharma make HuiKe kneel before telling him to wait till snow turns red
00:18:31 | Master Answer
00:23:16 | Discussion: How does HuiKe survive
00:27:05 | Discussion: Sharing the Dharma with others
00:31:14 | Did Malcom dye his hair?
00:31:47 | Back to Discussion: Sharing Dharma with others
00:35:05 | Back to slide 48: Bodhidharma ask his disciple to say something to demonstrate their understanding
00:36:51 | Slide 49: DaoFu's answer
00:37:36 | Slide 50: ZongChi's answer
00:38:00 | Slide 51 DaoYu's answer
00:39:34 | Slide 52 HuiKe Bowed
00:39:49 | Elaborate on DaoFu's answer
00:41:28 | Elaborate on ZongChi's answer
00:48:28 | Chinese of DaoYu's answer: 四大本空，五陰非有，而我見處，無一法可得
00:54:15 | Elaborate on DaoYu's answer
01:00:15 | Discussion: Why does DaoYu's answer demonstrate a deeper level of wisdom
01:09:15 | Word of Caution: Know your limitations. Do not comment on people who have more wisdom than you
 01:10:01 | Master answers: Why is DaoYu's wisdom higher
01:13:17 | Elaborate on HuiKe's response
01:14:59 | How Chan people compliment students: You are my bone marrow
01:15:39 | Malcom said he did not dye his hair, master calls him liar liar pants on fire
01:16:34 | Malcom question: what does "You have my bone marrow" mean, you are the same as me?
01:16:51 | Master answer
01:19:06 | Jane translates "Liar liar pants on fire" to Chinese
01:20:47 | Slide 53: 吾本來茲土，傳法救迷情，一花開五葉，結果自然成
01:24:56 | Slide 54
01:25:45 | Slide 55
01:26:14 | Slide 56
01:26:41 | Diego predicted that master will be seen walking in the Bahamas after he's done
01:27:16 | Slide 57
01:27:45 | Slide 58
01:28:17 | Slide 59: WeiTuo bodhisattva stood in guard when Ven. HuiKe is born
01:29:10 | Slide 60: parents thereupon named their son ShenGuang-Spritual light
01:29:47 | Slide 61
01:31:32 | Slide 62: Death of his parents cause HuiKe to turn to Buddhism
02:01:58 | Lecture ended on page 90'''

def main(argv):
    transcript=webvtt.from_sbv(FLAGS.transcript)

    segments=[]

    for l in desc.split("\n"):
        t=time.fromisoformat(l.split("|")[0].strip())
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