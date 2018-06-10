#!/usr/bin/python3

#add two images NOTE: both the two images have the same width and height the only be possible.

import numpy as np
import matplotlib  #.pyplot as pplt
import cv2
from PIL import Image

cv2.__version__

lichi=cv2.imread('/home/deepu/Desktop/directory/lichi.jpeg',1)
ball=cv2.imread('/home/deepu/Desktop/directory/ball.jpeg',1)
apple=cv2.imread('/home/deepu/Desktop/directory/apple.jpeg',1)
print(lichi.shape)
print(ball.shape)
edged = cv2.Canny(apple, 10, 200)
y=50
x=117
(h,w)=ball.shape[:2]
center=(w/2,h/2)

#rotate img by 180
M=cv2.getRotationMatrix2D(center,60,1.0)
rotated=cv2.warpAffine(ball ,M ,(w,h))

crop_img=lichi[y:y+h, x:x+w]

#print(lichi.histogram())
# Blending the images with 0.3 and 0.7
img = cv2.addWeighted(lichi, 0.3, rotated, 0.7, 0)        #alpha factor ---> this can only be 0  or 1
cv2.imwrite("xyz.png",img)           

# Show the image
cv2.imshow('image', img)
cv2.imshow('ball',rotated)
cv2.imshow('openimg',crop_img)
cv2.imshow('caany_window',edged)
# Wait for a key
cv2.waitKey(0)
# Distroy all the window open
cv2.distroyAllWindows()






























