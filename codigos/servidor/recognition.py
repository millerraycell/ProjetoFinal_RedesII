import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

img = cv2.imread("qr_img.png")

decodeObject = pyzbar.decode(img)

for obj in decodeObject:
    print(str(obj.data))