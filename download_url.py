import requests

urls=["http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_03.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_04.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_05.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_preface_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_03.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_04.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_05.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_06.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_07.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_07.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_07.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_08.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_08.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_08.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_09.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_09.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_09.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_10.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_10.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_10.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_11.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_11.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door1_11.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_03.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_04.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_05.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_06.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_07.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_07.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_07.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_08.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_08.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_08.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_09.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_09.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_09.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_10.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_10.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_10.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_11.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_11.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_11.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_12.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_12.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_12.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_13.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_13.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_13.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_14.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_14.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_14.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_15.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_15.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_15.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_16.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_16.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_16.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_17.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_17.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_17.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_18.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_18.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_18.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_19.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_19.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_19.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_20.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_20.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_20.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_21.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_21.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_21.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_22.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_22.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_22.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_23.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_23.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_23.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_24.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_24.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_24.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_25.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_25.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_25.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_26.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_26.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_26.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_27.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_27.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_27.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_28.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_28.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door2_28.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_03.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_04.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_05.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_06.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_07.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_07.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_07.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_bu-jiang.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_bu-jiang.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_bu-jiang.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_08.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_08.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_08.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_09.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_09.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_09.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_10.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_10.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_10.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_11.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_11.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door3_11.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door4_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door4_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door4_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door4_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door4_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door4_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_03.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_04.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_05.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door5_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_03.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_04.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_05.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_06.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door6_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door7_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door7_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door7_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door7_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door7_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door7_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door8_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door8_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door8_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door8_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door8_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door8_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door8_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door8_03.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door8_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_03.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_04.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_04.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_05.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_05.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_06.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_06.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_07.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_07.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_07.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_08.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_08.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_08.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_09.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_09.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door9_09.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door10_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door10_01.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door10_01.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door10_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door10_02.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door10_02.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door10_03.mp3","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door10_03.mp3.m3u","http://mp3.drbachinese.org/online_audio/sutra_explanation/HuaYanJingShu/HuaYanJingShu_Xuan_Hua_Shang_Ren_door10_03.mp3"]

for url in urls:
  if url.endswith('.m3u'):
    continue

  talk = requests.get(url)

  name='transcoded_video/'+url.split('/')[-1]
  with open(name, 'wb') as f:
    f.write(talk.content)