import cv2

image = cv2.imread("input.jpg")

rotated_180 = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow("180 Degree Rotation", rotated_180)
cv2.waitKey(0)
cv2.destroyAllWindows()
