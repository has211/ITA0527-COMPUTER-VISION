import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
    exit()

rows, cols = image.shape[:2]

# Define 4 points in original image
pts1 = np.float32([[50, 50],
                   [300, 50],
                   [50, 300],
                   [300, 300]])

# Define new positions
pts2 = np.float32([[0, 0],
                   [cols, 0],
                   [0, rows],
                   [cols, rows]])

# Get perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
perspective = cv2.warpPerspective(image, matrix, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()
