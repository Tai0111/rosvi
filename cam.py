#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2

def cam()
    cap = cv2.VideoCapture(0)

    while( cap.isOpened() ):

        ret, frame = cap.read()
        cv2.imshow('Capture',frame)
        key = cv2.waitKey(1)
        #print( '%08X' % (key&0xFFFFFFFF) )

        if key & 0x00FF  == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__' :
    print ('これはカメラモジュールです．importしてください.')
