


from absl import app, flags, logging
import json
import os
import webvtt
from datetime import time

FLAGS = flags.FLAGS

flags.DEFINE_string('transcript', None, '')


desc='''00:00 | 🙏 Emitofuo 
01:00 | Requesting the Dharma
04:29 | Invocations
07:34 | Date and Place
07:44 | Introduction
07:55 | Slide 45
12:40 | Slide 46
14:01 | Slide 47
16:22 | Slide 48
18:07 | Anthony Question: Why did Bodhidharma make HuiKe kneel before telling him to wait till snow turns red
18:31 | Master Answer
23:16 | Discussion: How does HuiKe survive
27:05 | Discussion: Sharing the Dharma with others
31:14 | Did Malcom dye his hair?
31:47 | Back to Discussion: Sharing Dharma with others
35:05 | Back to slide 48: Bodhidharma ask his disciple to say something to demonstrate their understanding
36:51 | Slide 49: DaoFu's answer
37:36 | Slide 50: ZongChi's answer
38:00 | Slide 51 DaoYu's answer
39:34 | Slide 52 HuiKe Bowed
39:49 | Elaborate on DaoFu's answer
41:28 | Elaborate on ZongChi's answer
48:28 | Chinese of DaoYu's answer: 四大本空，五陰非有，而我見處，無一法可得
54:15 | Elaborate on DaoYu's answer
1:00:15 | Discussion: Why does DaoYu's answer demonstrate a deeper level of wisdom
1:09:15 | Word of Caution: Know your limitations. Do not comment on people who have more wisdom than you
 1:10:01 | Master answers: Why is DaoYu's wisdom higher
1:13:17 | Elaborate on HuiKe's response
1:14:59 | How Chan people compliment students: You are my bone marrow
1:15:39 | Malcom said he did not dye his hair, master calls him liar liar pants on fire
1:16:34 | Malcom question: what does "You have my bone marrow" mean, you are the same as me?
1:16:51 | Master answer
1:19:06 | Jane translates "Liar liar pants on fire" to Chinese
1:20:47 | Slide 53: 吾本來茲土，傳法救迷情，一花開五葉，結果自然成
1:24:56 | Slide 54
1:25:45 | Slide 55
1:26:14 | Slide 56
1:26:41 | Diego predicted that master will be seen walking in the Bahamas after he's done
1:27:16 | Slide 57
1:27:45 | Slide 58
1:28:17 | Slide 59: WeiTuo bodhisattva stood in guard when Ven. HuiKe is born
1:29:10 | Slide 60: parents thereupon named their son ShenGuang-Spritual light
1:29:47 | Slide 61
1:31:32 | Slide 62: Death of his parents cause HuiKe to turn to Buddhism
2:01:58 | Lecture ended on page 90'''

def main(argv):
    transcript=webvtt.from_sbv(FLAGS.transcript)

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