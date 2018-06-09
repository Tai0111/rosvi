#!/usr/bin/env python
# --utf-8--

'''
prgname : RosVI.py
producer : Taichi Nakashima
discription : This app is an in-home operation system using speech recognition and image recognition.
'''

import socket
import xml.etree.ElementTree as ET
import os
import subprocess
import time
import string

import analysis
import jtalk

host = "10.0.1.2"
port = 10500
script = "./script/start_julius.sh"

def main():

    print ("Starting RosVI now...")

    p = subprocess.Popen([script], stdout=subprocess.PIPE, shell=True) # julius起動スクリプトを実行
    pid = str(p.stdout.read().decode('utf-8')) # juliusのプロセスIDを取得
    time.sleep(3) # 3秒間スリープ
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port)) #サーバーモードで起動したjuliusに接続

    print ("Recognition Start")
    jtalk.responce('start')

    try:
        data = '' # dataの初期化
        killword ='' # 前回認識した言葉を記憶するための変数
        first_time = 'yes' #初回の認識をスルーするため
        #time.sleep(3)
        while True:

            #print(data) # 認識した言葉を表示して確認
            if '</RECOGOUT>\n.' in data:

                root = ET.fromstring('<?xml version="1.0"?>\n' + data[data.find('<RECOGOUT>'):].replace('\n.', ''))
                for whypo in root.findall('./SHYPO/WHYPO'):

                    word = whypo.get('WORD') # juliusで認識したWORDをwordに入れる
                    score = float(whypo.get('CM')) # 認識した単語の閾値

                    print (word)
                    print (score)

                    if word == u'ロズビー' and score > 0.95:
                        #julius 停止
                        p.kill()
                        subprocess.call(["kill " + pid], shell=True)# juliusのプロセスを終了する。
                        client.close()    # docomoAPIとの競合を避けるためjuliusを一時停止

                        #docomo_APIによる高精度認識
                        jtalk.responce('responce')
                        time.sleep(2)
                        analysis.recognize()

                        #julius 再起動
                        p = subprocess.Popen([script], stdout=subprocess.PIPE, shell=True) # julius起動スクリプトを実行
                        pid = str(p.stdout.read().decode('utf-8')) # juliusのプロセスIDを取得
                        time.sleep(1) # 1秒間スリープ
                        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client.connect((host, port)) #サーバーモードで起動したjuliusに接続

                    data = '' # dataの初期化
            else:
                data += str(client.recv(1024).decode('utf-8')) #dataが空のときjuliusからdataに入れる
                #print('NotFound')# juliusに認識する言葉がない。認識していない。

    except KeyboardInterrupt:
        p.kill()
        subprocess.call(["kill " + pid], shell=True)# juliusのプロセスを終了する。
        client.close()

if __name__ == "__main__":
    main()
