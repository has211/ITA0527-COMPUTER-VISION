import cv2

cap = cv2.VideoCapture("video.mp4")
frames=[]

while True:
    ret,frame=cap.read()
    if not ret:
        break
    frames.append(frame)

for frame in reversed(frames):
    cv2.imshow("Reverse Slow",frame)
    if cv2.waitKey(100)==27:
        break
