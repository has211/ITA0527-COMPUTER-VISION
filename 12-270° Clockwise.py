import cv2

image = cv2.imread("input.jpg")

rotated_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("270 Degree Rotation", rotated_270)
cv2.waitKey(0)
cv2.destroyAllWindows()
