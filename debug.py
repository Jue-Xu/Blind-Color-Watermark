import re
import os
import cv2
import math
import time
import socket
import pyperclip
import numpy as np
from cv2 import cv
from matplotlib import pyplot as plt
from PIL import Image,ImageDraw,ImageFont,ImageGrab

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
present_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

#################################################################
def num2bin(ip):
    bin_ip = map('{0:08b}'.format, map(int, ip.split('.')))
    return bin_ip

def bin2num(bin_ip):
    ip = map('{0:d}'.format, map(int, bin_ip))
    return ip

#################################################################
bin_ip = num2bin(ip)
array_bin_ip = np.array(map(int, list(bin_ip[0]+bin_ip[1]+bin_ip[2]+bin_ip[3])))

#################################################################
img = cv2.imread('win.png', 1)
(B,G,R) = cv2.split(img)
new_Y = np.float32(B.copy())

for i in range(32):
    before_array_dct = np.float32(B[0:8,0+8*i:8+8*i])
    after_array_dct = cv2.dct(before_array_dct)
    before_array_idct = after_array_dct.copy()
    before_array_idct[7,7] = 100*array_bin_ip[i]
    after_array_idct = cv2.idct(before_array_idct)
    new_Y[0:8,0+8*i:8+8*i] = after_array_idct

new_img = img.copy()
new_img[:,:,0] = new_Y
cv2.imwrite('debug.png', new_img)
