import cv2

def play_reverse_slow(video_path):

    cap = cv2.VideoCapture(video_path)
    frames = []

    # Read frames from video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    # Play frames in reverse
    for frame in reversed(frames):

        # Resize frame to avoid zoomed display
        frame = cv2.resize(frame, (800, 600))

        cv2.imshow("Reverse Slow Motion Video", frame)

        # Slow motion delay
        if cv2.waitKey(60) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


# Run function
play_reverse_slow("video.mp4")
