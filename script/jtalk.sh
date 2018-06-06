#!/bin/sh
TMP=test.wav
echo "$1" | open_jtalk \
-m /usr/share/hts-voice/mei/mei_normal.htsvoice \
-x /var/lib/mecab/dic/open-jtalk/naist-jdic \
-ow $TMP && \
aplay -Dhw:1,0 --quiet $TMP
rm -f $TMP
