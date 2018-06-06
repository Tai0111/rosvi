#!/usr/bin/env python
# -*- coding: utf-8 -*-

#マイク0番からの入力を受ける。一定時間(RECROD_SECONDS)だけ録音し、ファイル名：mono.wavで保存する。

import pyaudio
import sys
import time
import wave
import subprocess

import jtalk

#音声メッセージの録音
def rec():

    script = "./script/jtalk.sh"
    mes = "こんにちは"

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
    #subprocess.Popen([script]+[mes.encode('utf-8')], stdout=subprocess.PIPE, shell=True)
    #jtalk起動分だけ停止
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

if __name__ == '__main__' :
    print ('これは録音モジュールです．importしてください.')
