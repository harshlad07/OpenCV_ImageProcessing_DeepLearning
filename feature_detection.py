import cv2
import numpy as np

img = cv2.imread('i1.jpg', 0)
img1_resize = cv2.resize(img, (500, 500))
img2 = cv2.imread('rickmorty.jpg', 0)
img2_resize = cv2.resize(img2, (500, 500))

# Creating object for ORB_create
orb = cv2.ORB_create()

# Detect and compute image 1
kp1, des1 = orb.detectAndCompute(img1_resize, None)
# kp1, des1 = orb.detectAndCompute(img, None)

# Detect and compute image 2
kp2, des2 = orb.detectAndCompute(img2_resize, None)
# kp2, des2 = orb.detectAndCompute(img2, None)

# Create object for BFMatcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
match = sorted(matches, key=lambda x:x.distance)

print(len(matches))
outImg = np.empty((1,1))
# final_match = cv2.drawMatches(img,kp1,img2,kp2, matches[:12], outImg, flags=2)
final_match = cv2.drawMatches(img1_resize,kp1,img2_resize,kp2, matches[:12], outImg, flags=2)

cv2.imshow('feature_match', final_match)
cv2.waitKey(0)
