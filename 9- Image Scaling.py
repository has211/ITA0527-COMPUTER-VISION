import cv2

image = cv2.imread("input.jpg")

if image is None:
    print("Image not found!")
    exit()

# Resize smaller
small = cv2.resize(image, (300, 300))

# Resize bigger
big = cv2.resize(image, (800, 800))

cv2.imshow("Original Image", image)
cv2.imshow("Smaller Image", small)
cv2.imshow("Bigger Image", big)

cv2.waitKey(0)
cv2.destroyAllWindows()
