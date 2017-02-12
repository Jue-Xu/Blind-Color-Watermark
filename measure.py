import re
import cv2
import math
import time
import socket
import numpy as np
from cv2 import cv
from matplotlib import pyplot as plt
from PIL import Image,ImageDraw,ImageFont,ImageGrab

measure = cv2.imread('debug.png', 1)
(B,G,R) = cv2.split(measure)
restore_bin = np.zeros(32)

for i in range(32):
    measure_dft = cv2.dct(np.float32(B[0:8,0+8*i:8+8*i]))
    if measure_dft[7,7] > 50:
        restore_bin[i] = 1

restore_bin_array = np.array(map(int, restore_bin)).reshape((4,8))
restore_ip = np.zeros(4)
for i in range(4):
    for j in range(8):
        restore_ip[i] = restore_ip[i] + restore_bin_array[i][j]*2**(7-j)

print str(int(restore_ip[0]))+'.'+str(int(restore_ip[1]))+'.'+str(int(restore_ip[2]))+'.'+str(int(restore_ip[3]))
