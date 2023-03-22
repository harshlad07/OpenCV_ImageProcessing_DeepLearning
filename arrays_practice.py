import numpy as np
import matplotlib as plt
import cv2

#Read
read = cv2.imread('i1.jpg')
print(type(read))
print(read.shape)
read2 = cv2.imread('i2.jpg')
print(read2.shape)
print(type(read2))

#Resize
rr1 = cv2.resize(read, (200,200))
rr2 = cv2.resize(read2, (200,200))

#Join arrays of 2 images
join  = np.concatenate((rr1, rr2), axis=1)
print(type(join))
# print(join)

#Merge 2 images
add = cv2.addWeighted(rr1, 0.5, rr2, 0.5, 0)
op = cv2.imwrite('output.jpg', add)

#Create a black image using zeroes and ones
img = np.zeros((350, 500, 3), dtype =np.uint8)
cv2.imshow('black image', img)
# print(img)

img2 = np.ones((300, 255, 3), dtype = np.uint8)
img2 =img2 * 255
cv2.imshow('black image2', img2)
# print(img2)

cv2.waitKey(0)