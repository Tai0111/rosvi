#!/usr/bin/env python
# --utf-8--

'''
prgname : func.py
producer : Taichi Nakashima
discription : This is a module that stores functions for RosVI
'''

import subprocess

def IR(c):
    if c == 'on':
        args = ['irsend', '-#', '1', 'SEND_ONCE', 'Light', 'on']
        subprocess.Popen(args)
    elif c == 'off':
        args = ['irsend', '-#', '1', 'SEND_ONCE', 'Light', 'off']
        subprocess.Popen(args)


if __name__ == '__main__':
    print ("これはRosVI用の各機能を格納したモジュールです，importして利用してください．")
