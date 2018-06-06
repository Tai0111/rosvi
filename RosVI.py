#!/usr/bin/env python
# --utf-8--

'''
prgname : RosVI.py
producer : Taichi Nakashima
discription : This app is an in-home operation system using speech recognition and image recognition.
'''

import analysis
import audio

#audio.rec()
command = analysis.recognize()
print (command)
