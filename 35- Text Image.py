import cv2
import numpy as np

text = input("Enter text: ")

img = np.ones((500,500,3),dtype="uint8")*255
cv2.putText(img,text,(100,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow("Text Image",img)
cv2.waitKey(0)
