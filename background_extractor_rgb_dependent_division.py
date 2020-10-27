#!/usr/bin/python3

#./background_extractor3.py videoplayback2.mp4 processed4.avi 1

#(RGB)
#USING LOOP

import numpy as np
import cv2
import sys
from os import path

try:
    input_str = str(sys.argv[1])
except:
    raise ValueError("Input file not specified")

if((path.isfile(input_str))):
    print(f"Loading {input_str}")
    cap = cv2.VideoCapture(input_str)
else:
    raise ValueError("Input file does not exist")

try:
    output_str = str(sys.argv[2])
except:
    raise ValueError("Output filename not specified")

try:
    division = int(sys.argv[3])
except:
    division = 1

frameSize = (640,720)
out = cv2.VideoWriter(output_str,cv2.VideoWriter_fourcc(*'DIVX'),24.0,frameSize)

depth = int(256/division) + (256 % division != 0)
print(depth**3,"Colors")

maximum = np.zeros((360,640,depth,depth,depth)).astype(np.uint8)

output_frame = np.zeros((720,640,3),dtype=np.uint8)
frame_no = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    frame_no += 1
    print("Frame no:",frame_no)
    #print(np.max(frame,axis=2))

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for m in range(frame.shape[0]):
       for n in range(frame.shape[1]):
           maximum[m,n,int(frame[m,n,0]/division),
                   int(frame[m,n,1]/division),
                   int(frame[m,n,2]/division)] += 1

           max_index = np.array(np.unravel_index(np.argmax(maximum[m,n]),(depth,depth,depth)))
           output_frame[m,n,:] = (division*max_index)

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
