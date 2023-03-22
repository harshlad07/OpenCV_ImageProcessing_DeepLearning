import cv2
import numpy as np

# img = cv2.imread('rickmorty.jpg')
# meadian = np.median(img)
# print(meadian)
# lower_bound = int(max(0, 0.7*meadian))
# upper_bound = int(min(255, 1.3*meadian))
# print('lower_bound = ', lower_bound)
# print('upper_bound = ', upper_bound)
# edge = cv2.Canny(img, lower_bound, upper_bound+100)
# store = cv2.imwrite('rickmorty_lu_bounds.jpg', edge)


img2 = cv2.imread('rickmorty.jpg')
blur_image = cv2.blur(img2, ksize=(5,5))
cv2.findChessboardCorners()
meadian = np.median(blur_image)
print(meadian)
lower_bound = int(max(0, 0.7*meadian))
upper_bound = int(min(255, 1.3*meadian))
print('lower_bound = ', lower_bound)
print('upper_bound = ', upper_bound)
edge = cv2.Canny(blur_image, lower_bound, upper_bound+100)
store = cv2.imwrite('rickmorty_blur_lu_bounds.jpg', edge)