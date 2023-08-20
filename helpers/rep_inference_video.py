import cv2
import os
import tempfile
import uuid
from ultralytics import YOLO

def reproduce_video(path_model, path_video, consecutive_frames=5, cooldown=15):
    # Load the YOLOv8 model
    model = YOLO(path_model)

    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(path_video.read())

    # Open the video file
    cap = cv2.VideoCapture(tfile.name)

    # Initialize the VideoWriter outside the loop
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    processed_video_path =  f'./videos/streamlit_video_{uuid.uuid4()}.mp4'
    cap_out = cv2.VideoWriter(processed_video_path, fourcc, fps, (frame_width, frame_height))

    total_kicks, total_punches, total_grappling = 0, 0, 0
    kick_cooldown, punch_cooldown, grappling_cooldown = 0, 0, 0
    kick_counter, punch_counter, grappling_counter = 0, 0, 0

    name_map = None

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame)

            # Check if boxes are not empty
            if results[0].boxes:
                # If name_map is None, then populate it
                if name_map is None:
                    name_map = results[0].names

                detections = results[0].boxes.data.tolist()

                detected_classes = set([name_map[int(det[-1])] for det in detections])

                if 'kick' in detected_classes:
                    kick_counter += 1
                    if kick_counter >= consecutive_frames and kick_cooldown <= 0:
                        total_kicks += 1
                        kick_cooldown = cooldown
                        kick_counter = 0  # Reset counter after confirming a kick
                else:
                    kick_counter = 0

                if 'punch' in detected_classes:
                    punch_counter += 1
                    if punch_counter >= consecutive_frames and punch_cooldown <= 0:
                        total_punches += 1
                        punch_cooldown = cooldown
                        punch_counter = 0  # Reset counter after confirming a punch
                else:
                    punch_counter = 0

                if 'grappling' in detected_classes:
                    grappling_counter += 1
                    if grappling_counter >= consecutive_frames and grappling_cooldown <= 0:
                        total_grappling += 1
                        grappling_cooldown = cooldown
                        grappling_counter = 0
                else:
                    grappling_counter = 0

            # Decrement the cooldowns
            if kick_cooldown > 0:
                kick_cooldown -= 1
            if punch_cooldown > 0:
                punch_cooldown -= 1
            if grappling_cooldown > 0: 
                grappling_cooldown -= 1

            # Visualize the results on the frame with kick and punch counts
            annotated_frame = results[0].plot()
            y_offset = frame_height - 30
            cv2.putText(annotated_frame, f'Kicks: {total_kicks}', (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(annotated_frame, f'Punches: {total_punches}', (10, y_offset - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(annotated_frame, f'Grappling: {total_grappling}', (10, y_offset - 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

            # Display the annotated frame, however, this is triggering an error in Streamlit
            # cv2.imshow("YOLOv8 Inference", annotated_frame)

            # Write the annotated frame to the output video
            cap_out.write(annotated_frame)

            # Break the loop if 'q' is pressed
            # if cv2.waitKey(1) & 0xFF == ord("q"):
            #     break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture and writer objects, and close the display window
    cap.release()
    cap_out.release()
    # cv2.destroyAllWindows()

    print(f"Total Kicks: {total_kicks}")
    print(f"Total Punches: {total_punches}")
    print(f"Total Grappling: {total_grappling}")

    tfile.close()
    os.unlink(tfile.name)

    return processed_video_path