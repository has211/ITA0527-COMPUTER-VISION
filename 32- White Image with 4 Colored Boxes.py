import cv2
import numpy as np

h = int(input("Height: "))
w = int(input("Width: "))

img = np.ones((h,w,3), dtype="uint8")*255

box_h = h//10
box_w = w//10

img[0:box_h,0:box_w] = (0,0,0)
img[0:box_h,w-box_w:w] = (255,0,0)
img[h-box_h:h,0:box_w] = (0,255,0)
img[h-box_h:h,w-box_w:w] = (0,0,255)

cv2.imshow("Boxes",img)
cv2.waitKey(0)
