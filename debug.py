import re
import os
import cv2
import math
import time
import socket
import pyperclip
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageGrab

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
present_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

#################################################################
def num2bin(ip):
    bin_ip = map('{0:08b}'.format, map(int, ip.split('.')))
    return bin_ip

#################################################################
bin_ip = num2bin(ip)
array_bin_ip = np.array(map(int, list(bin_ip[0]+bin_ip[1]+bin_ip[2]+bin_ip[3])))

#################################################################
while True:
    im = ImageGrab.grabclipboard()
    if im != None:
        im.save('img.png','PNG')
        pyperclip.copy("")
#################################################################
        img = cv2.imread('img.png', 1)
        os.remove('img.png')
        a = 10
        w, h = img.shape[:2]
        (B,G,R) = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2YUV))
        new_Y = np.float32(B.copy())

        for i in range(32):
            before_array_dct = new_Y[w-4:w,0+4*i:0+4*(i+1)]
            after_array_dct = cv2.dct(before_array_dct)
            before_array_idct = after_array_dct.copy()
            before_array_idct[3,3] = a*array_bin_ip[i]
            after_array_idct = cv2.idct(before_array_idct)
            maxium = max(after_array_idct.flatten())
            minium = min(after_array_idct.flatten())
            if maxium > 255:
                after_array_idct = after_array_idct - (maxium - 255)
            if minium < 0:
                after_array_idct = after_array_idct - minium
            new_Y[w-4:w,0+4*i:0+4*(i+1)] = after_array_idct

        new_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        new_img[:,:,0] = new_Y
        after_convert = cv2.cvtColor(new_img, cv2.COLOR_YUV2BGR)
        cv2.imwrite('watermark.png', after_convert)
    time.sleep(1)
