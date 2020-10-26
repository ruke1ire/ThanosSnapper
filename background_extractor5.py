#!/usr/bin/python3

#BW
#NO LOOP

#./background_extractor5.py videoplayback2.mp4 processed7.avi 1

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

maximum = np.zeros((360,640,depth)).astype(np.uint8)

output_frame = np.zeros((720,640,3),dtype=np.uint8)
frame_no = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    frame_no += 1
    print("Frame no:",frame_no)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    x_range = np.arange(frame.shape[0])
    y_range = np.arange(frame.shape[1])
    xx, yy = np.meshgrid(x_range,y_range)
    xx = xx.flatten()
    yy = yy.flatten()

    maximum[xx,yy,(gray[:,:].T.flatten()/division).astype(int)] += 1

    output_frame[:360,:640,0] = (division*np.argmax(maximum,axis=2)).astype(np.uint8)
    output_frame[:360,:640,1] = (division*np.argmax(maximum,axis=2)).astype(np.uint8)
    output_frame[:360,:640,2] = (division*np.argmax(maximum,axis=2)).astype(np.uint8)

    output_frame[360:,:640,:] = frame

    out.write(output_frame.astype(np.uint8))

    cv2.imshow('frame',output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


