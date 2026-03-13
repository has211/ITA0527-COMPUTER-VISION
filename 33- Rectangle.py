import cv2
import numpy as np

img = np.ones((500,500,3),dtype="uint8")*255
cv2.rectangle(img,(100,100),(400,300),(0,0,255),3)

cv2.imshow("Rectangle",img)
cv2.waitKey(0)
