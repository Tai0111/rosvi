#!/bin/bash

export ALSEDEV="plughw:0,0"
modprobe snd-pcm-oss

~/work/julius-4.4.2.1/julius/julius -C ~/work/julius-4.4.2.1/kit/dictation-kit-v4.4/word.jconf -module > /dev/null &
echo $!
sleep 2
