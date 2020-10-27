#!/usr/bin/python3

#RGB
#NO LOOP

#./background_extractor_rgb_division.py ./resources/videoplayback2.mp4 output.avi 1

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

inputSize = (360,640)
frameSize = (inputSize[1],inputSize[0]*2)
out = cv2.VideoWriter(output_str,cv2.VideoWriter_fourcc(*'DIVX'),24.0,frameSize)

depth = int(256/division) + (256 % division != 0)
print(depth**3,"Colors")

red_maximum = np.zeros((inputSize[0],inputSize[1],depth)).astype(np.uint8)
green_maximum = np.zeros((inputSize[0],inputSize[1],depth)).astype(np.uint8)
blue_maximum = np.zeros((inputSize[0],inputSize[1],depth)).astype(np.uint8)

output_frame = np.zeros((frameSize[1],frameSize[0],3),dtype=np.uint8)
frame_no = 0

x_range = np.arange(inputSize[0])
y_range = np.arange(inputSize[1])
xx, yy = np.meshgrid(x_range,y_range)
xx = xx.flatten()
yy = yy.flatten()

while(cap.isOpened()):
    ret, frame = cap.read()
    frame_no += 1
    print("Frame no:",frame_no)

    red_maximum[xx,yy,(frame[:,:,0].T.flatten()/division).astype(int)] += 1
    green_maximum[xx,yy,(frame[:,:,1].T.flatten()/division).astype(int)] += 1
    blue_maximum[xx,yy,(frame[:,:,2].T.flatten()/division).astype(int)] += 1

    output_frame[:inputSize[0],:inputSize[1],0] = (division*np.argmax(red_maximum,axis=2)).astype(np.uint8)
    output_frame[:inputSize[0],:inputSize[1],1] = (division*np.argmax(green_maximum,axis=2)).astype(np.uint8)
    output_frame[:inputSize[0],:inputSize[1],2] = (division*np.argmax(blue_maximum,axis=2)).astype(np.uint8)

    output_frame[inputSize[0]:,:inputSize[1],:] = frame

    out.write(output_frame.astype(np.uint8))

    cv2.imshow('frame',output_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

