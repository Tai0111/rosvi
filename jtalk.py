#coding: utf-8
import subprocess
import time

import func
import cam

#jtalkの発話
def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    outwav=['-ow','audio/jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t.encode('utf-8'))
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-Dhw:1,0','-q','audio/jtalk.wav']
    wr = subprocess.Popen(aplay)
    #time.sleep(3)

#analysis.pyから受けた命令ごとに分類
def order(t):
    #命令ごとの機能を実行
    if "電気" in t:
        if "つけて" in t:
            responce('light_on')
            time.sleep(2)
            func.IR('on')
        elif "けして" in t or "消して" in t:
            responce('light_off')
            time.sleep(2)
            func.IR('off')
        else:
            responce('errer')

    elif "カメラ" in t or "部屋" in t:
        if "見せて" in t or "見して" in t or "つけて" in t:
            responce('camera')

    else:
        responce('errer')
        print (t)

#受け取った命令別の返事と機能の実行
def responce(p):
    if p == 'start':
        text = 'ルームオペレーティングシステム，ロズビー，起動しました．'
        jtalk(text)

    elif p == 'responce':
        text = 'はい，お呼びでしょうか．'
        jtalk(text)

    elif p == 'light_on':
        text = '電気をつけますね．'
        jtalk(text)

    elif p == 'light_off':
        text = '電気を消しますね．'
        jtalk(text)

    elif p == 'camera':
        text = 'カメラの映像を表示します．'
        jtalk(text)
        cam.cam()


    elif p == 'errer':
        text = 'ごめんなさい，聞き取れませんでした．'
        jtalk(text)

if __name__ == '__main__':
    print ("これはJtak用モジュールです，importして利用してください．")
