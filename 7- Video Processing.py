import cv2

cap = cv2.VideoCapture("video.mp4")  # Use 0 for webcam

if not cap.isOpened():
    print("Error opening video")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Normal Speed", frame)

    # Slow motion (increase delay)
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
