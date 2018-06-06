#coding: utf-8
import subprocess

#jtalkの発話
def jtalk(t):
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    outwav=['-ow','open_jtalk.wav']
    cmd=open_jtalk+mech+htsvoice+outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t.encode('utf-8'))
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-Dhw:1,0','-q','open_jtalk.wav']
    wr = subprocess.Popen(aplay)

#analysis.pyから受けた命令ごとに分類
def order(t):
    #命令ごとの機能を実行
    if "電気" in t:
        if "つけて" in t:
            responce('light_on')
        elif "けして" in t or "消して" in t:
            responce('light_off')

#受け取った命令別の返事と機能の実行
def responce(p):
    if p == 'start':
        text = 'はい，お呼びでしょうか'
        jtalk(text)
    elif p == 'light_on':
        text = '電気をつけますね'
        jtalk(text)
    elif p == 'light_off':
        text = '電気を消しますね'
        jtalk(text)

if __name__ == '__main__':
    responce()
