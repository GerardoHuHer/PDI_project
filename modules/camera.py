import cv2


def start_camera(process_frame_callback):
    """
    Starts the camera and passes each frame to the callback function for processing.
    Args:
        process_frame_callback (function): Function to process each frame.
    """
    cap = cv2.VideoCapture(0)  # Open default webcam
    if not cap.isOpened():
        raise Exception("Could not open webcam.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame with the provided callback
        processed_frame = process_frame_callback(frame)

        # Show the processed frame
        cv2.imshow("Real-Time AR Tool", processed_frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
