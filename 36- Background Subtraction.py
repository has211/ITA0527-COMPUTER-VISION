import cv2

img = cv2.imread("input.jpg")
lower = (0,0,0)
upper = (100,100,100)

mask = cv2.inRange(img, lower, upper)

cv2.imshow("Background Removed",mask)
cv2.waitKey(0)
