import cv2

img = cv2.imread("input.jpg")
lower = (100,100,100)
upper = (255,255,255)

mask = cv2.inRange(img, lower, upper)

cv2.imshow("Foreground Extracted",mask)
cv2.waitKey(0)
