import cv2
import numpy as np

img = np.ones((500,500,3),dtype="uint8")*255
cv2.circle(img,(250,250),100,(255,0,0),3)

cv2.imshow("Circle",img)
cv2.waitKey(0)
