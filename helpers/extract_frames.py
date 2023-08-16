from download_from_youtube import download_path
import cv2

# Define a function to extract frames
def extract_frames(video_path, interval=20):
    """Extract frames from a video using OpenCV."""
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    frames = []
    while success:
        if count % interval == 0:  # save frame every 'interval' frames
            frames.append(image)
        success, image = vidcap.read()
        count += 1
    vidcap.release()
    return frames

frames = extract_frames(download_path, interval=10)  # Extracts every 30th frame

# Optionally, you can save the frames to disk if required
for idx, frame in enumerate(frames):
    cv2.imwrite(f"./extracted_f/frame_{idx}.jpg", frame)