#!/usr/bin/env python
# --utf-8--

import requests
import json
import pyaudio
import sys
import time
import wave
import subprocess

import jtalk

#解析する音声の録音
def rec():
    #各種設定
    chunk = 512
    #APIの規定で16bitに設定
    FORMAT = pyaudio.paInt16
    #モノラル
    CHANNELS = 1
    #サンプリングレート,APIの規定で16kHzに設定
    RATE = 16000
    #録音時間
    RECORD_SECONDS = 3

    #pyaudio
    audio = pyaudio.PyAudio()
    #マイク0番を設定
    Mic_index = 0
    #マイクからデータ取得
    stream = audio.open(format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    input_device_index = Mic_index,
    frames_per_buffer = chunk)

    #--録音--
    print ('Recording now...')
    all = []
    for i in range(0, int(RATE / chunk * RECORD_SECONDS)):
        data = stream.read(chunk)
        all.append(data)
    print ('Finised Recording')
    #--録音--

    stream.stop_stream()
    stream.close()
    audio.terminate()

    out = wave.open('/home/taichi/RosVI/audio/command.wav','wb')
    out.setnchannels(CHANNELS) #mono
    out.setsampwidth(audio.get_sample_size(FORMAT)) #16bits
    out.setframerate(RATE)
    out.writeframes(b''.join(all))
    out.close()

#docomo音声認識APIによる解析
def recognize():
    #命令の取得(録音)
    rec()
    #ファイルの場所
    path = '/home/taichi/RosVI/audio/command.wav'
    #docomo音声認識API
    url = "https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY=593030457255434f45696f61737833635a59665132624a4c363939306279525351565535635864704e622e"
    wav_file = {"a": open(path, 'rb'), "v":"off"}
    #postしてけっかを取得
    result = requests.post(url, files=wav_file)
    responce = (result.json()['text'])

    jtalk.order(responce)

if __name__ == '__main__' :
    print ('これは音声認識モジュールです．importしてください.')
