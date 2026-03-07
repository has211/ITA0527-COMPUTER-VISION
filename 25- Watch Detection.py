import cv2

# Load main image
image = cv2.imread("watch_image.jpg")

# Load watch template
template = cv2.imread("watch_template.jpg")

h, w = template.shape[:2]

result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.8

loc = cv2.minMaxLoc(result)

top_left = loc[3]
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(image, top_left, bottom_right, (0,255,0), 2)

cv2.imshow("Watch Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
