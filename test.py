#!/usr/bin/python3

import cv2
import numpy as np

frameSize = (640,360)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'),20.0,frameSize)

for i in range(0,255):
    img = np.ones((360,640,3),dtype=np.uint8)*i
    out.write(img)

out.release()

