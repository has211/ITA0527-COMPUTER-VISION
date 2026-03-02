import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Apply Harris Corner Detection
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Dilate result for marking corners
corners = cv2.dilate(corners, None)

# Mark corners in red
image[corners > 0.01 * corners.max()] = [0, 0, 255]

cv2.imshow("Harris Corner Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
