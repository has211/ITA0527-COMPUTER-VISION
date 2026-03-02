import cv2
import numpy as np

# Read image
image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
    exit()

rows, cols = image.shape[:2]

# Define 3 points in original image
pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200]])

# Define new positions for those 3 points
pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250]])

# Create transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
affine = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", affine)

cv2.waitKey(0)
cv2.destroyAllWindows()
