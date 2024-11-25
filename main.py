import cv2
from modules.background import replace_background, adjust_hsv_thresholds

# Load background image
background_img = cv2.imread('assets/background.jpeg')

# Initialize HSV threshold adjustment
get_hsv_thresholds = adjust_hsv_thresholds()


def process_frame(frame):
    # Get current HSV thresholds from trackbars
    lower_hsv, upper_hsv = get_hsv_thresholds()

    # Apply background replacement
    return replace_background(frame, background_img, lower_hsv, upper_hsv)


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)  # Open webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame with background replacement
        processed_frame = process_frame(frame)

        # Show the result
        cv2.imshow("Real-Time Background Replacement", processed_frame)

        # Quit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
