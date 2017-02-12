import re
import cv2
import math
import time
import socket
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageGrab

measure = cv2.imread('watermark.png', 1)
w, h =measure.shape[:2]
(measure_B,measure_G,measure_R) = cv2.split(cv2.cvtColor(measure, cv2.COLOR_BGR2YUV))
restore_bin = np.zeros(32)

for i in range(32):
    measure_dft = cv2.dct(np.float32(measure_B[w-4:w,0+4*i:4+4*i]))
    if measure_dft[3,3] > 5:
        restore_bin[i] = 1

restore_bin_array = np.array(map(int, restore_bin)).reshape((4,8))
restore_ip = np.zeros(4)
for i in range(4):
    for j in range(8):
        restore_ip[i] = restore_ip[i] + restore_bin_array[i][j]*2**(7-j)

print str(int(restore_ip[0]))+'.'+str(int(restore_ip[1]))+'.'+str(int(restore_ip[2]))+'.'+str(int(restore_ip[3]))

time.sleep(10)
