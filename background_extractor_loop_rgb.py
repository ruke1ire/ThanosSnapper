#!/usr/bin/python3

#RGB
#USING LOOP

import numpy as np
import cv2
import sys

#np.set_printoptions(threshold=sys.maxsize)
cap = cv2.VideoCapture('./videoplayback.mp4')

frameSize = (720,720)
out = cv2.VideoWriter('processed2.avi',cv2.VideoWriter_fourcc(*'DIVX'),24.0,frameSize)

red_maximum = np.zeros((360,640,26)).astype(np.uint8)
green_maximum = np.zeros((360,640,26)).astype(np.uint8)
blue_maximum = np.zeros((360,640,26)).astype(np.uint8)

output_frame = np.zeros((720,720,3),dtype=np.uint8)
frame_no = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    frame_no += 1
    print(frame_no)
    #print(np.max(frame,axis=2))

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for m in range(frame.shape[0]):
       for n in range(frame.shape[1]):
           red_maximum[m,n,int(frame[m,n,0]/10)] += 1
           green_maximum[m,n,int(frame[m,n,1]/10)] += 1
           blue_maximum[m,n,int(frame[m,n,2]/10)] += 1

    output_frame[:360,:640,0] = (10*np.argmax(red_maximum,axis=2)).astype(np.uint8)
    output_frame[:360,:640,1] = (10*np.argmax(green_maximum,axis=2)).astype(np.uint8)
    output_frame[:360,:640,2] = (10*np.argmax(blue_maximum,axis=2)).astype(np.uint8)

    output_frame[360:,:640,:] = frame
    #print(np.max(output_frame,axis=2))
    #print(output_frame)
    out.write(output_frame.astype(np.uint8))

    cv2.imshow('frame',output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
