import cv2

image = cv2.imread("input.jpg")

rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("90 Degree Rotation", rotated_90)
cv2.waitKey(0)
cv2.destroyAllWindows()
