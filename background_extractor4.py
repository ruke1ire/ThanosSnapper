#!/usr/bin/python3

#RGB
#NO LOOP

#./background_extractor2.py videoplayback2.mp4 processed4.avi 1

import numpy as np
import cv2
import sys

try:
    input_str = str(sys.argv[1])
    output_str = str(sys.argv[2])
    try:
        division = int(sys.argv[3])
    except:
        division = 1
except:
    raise ValueError("Invalid Input/Output file names")

#np.set_printoptions(threshold=sys.maxsize)
cap = cv2.VideoCapture(input_str)

frameSize = (640,720)
out = cv2.VideoWriter(output_str,cv2.VideoWriter_fourcc(*'DIVX'),24.0,frameSize)

depth = int(256/division) + (256 % division != 0)
print(depth**3,"Colors")

red_maximum = np.zeros((360,640,depth)).astype(np.uint8)
green_maximum = np.zeros((360,640,depth)).astype(np.uint8)
blue_maximum = np.zeros((360,640,depth)).astype(np.uint8)

output_frame = np.zeros((720,640,3),dtype=np.uint8)
frame_no = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    frame_no += 1
    print("Frame no:",frame_no)

    x_range = np.arange(frame.shape[0])
    y_range = np.arange(frame.shape[1])
    xx, yy = np.meshgrid(x_range,y_range)
    xx = xx.flatten()
    yy = yy.flatten()

    print(xx)
    print((frame[:,:,0].flatten()/division).astype(int))

    red_maximum[xx,yy,(frame[:,:,0].T.flatten()/division).astype(int)] += 1
    green_maximum[xx,yy,(frame[:,:,1].T.flatten()/division).astype(int)] += 1
    blue_maximum[xx,yy,(frame[:,:,2].T.flatten()/division).astype(int)] += 1

    output_frame[:360,:640,0] = (division*np.argmax(red_maximum,axis=2)).astype(np.uint8)
    output_frame[:360,:640,1] = (division*np.argmax(green_maximum,axis=2)).astype(np.uint8)
    output_frame[:360,:640,2] = (division*np.argmax(blue_maximum,axis=2)).astype(np.uint8)

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

