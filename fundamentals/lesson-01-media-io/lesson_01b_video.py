from pathlib import Path
import cv2

lesson_folder = Path(__file__).resolve().parent
video_path = lesson_folder/"data"/"camera.mp4"

# Read video
video = cv2.VideoCapture(str(video_path))

# Check if video opened successfully
if not video.isOpened():
    raise IOError(f"Error opening video file: {video_path}")

# Read frames
retval = True
while retval:
    retval,image = video.read()

    if retval:
        cv2.imshow('Frame',image)
        cv2.waitKey(20)

video.release()
cv2.destroyAllWindows()