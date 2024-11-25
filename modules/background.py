import cv2
import numpy as np


def replace_background(frame, background_image, lower_hsv, upper_hsv):
    """
    Replace the background of the frame with a given image using improved thresholding.
    Args:
        frame (numpy.ndarray): The input frame.
        background_image (numpy.ndarray): The replacement background image.
        lower_hsv (tuple): Lower HSV range for background segmentation.
        upper_hsv (tuple): Upper HSV range for background segmentation.
    Returns:
        numpy.ndarray: Frame with replaced background.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    # Refine the mask
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask_inv = cv2.bitwise_not(mask)

    # Resize background
    background_resized = cv2.resize(background_image, (frame.shape[1], frame.shape[0]))
    foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)
    background = cv2.bitwise_and(background_resized, background_resized, mask=mask)
    return cv2.add(foreground, background)


def adjust_hsv_thresholds():
    """
    Create trackbars for dynamically adjusting HSV thresholds.
    Returns:
        function: A lambda function that retrieves the current trackbar values.
    """

    def nothing(x):
        pass

    # Create a window with trackbars
    cv2.namedWindow("Adjust HSV Thresholds")
    cv2.createTrackbar("Lower Hue", "Adjust HSV Thresholds", 0, 179, nothing)
    cv2.createTrackbar("Upper Hue", "Adjust HSV Thresholds", 179, 179, nothing)
    cv2.createTrackbar("Lower Saturation", "Adjust HSV Thresholds", 0, 255, nothing)
    cv2.createTrackbar("Upper Saturation", "Adjust HSV Thresholds", 255, 255, nothing)
    cv2.createTrackbar("Lower Value", "Adjust HSV Thresholds", 0, 255, nothing)
    cv2.createTrackbar("Upper Value", "Adjust HSV Thresholds", 255, 255, nothing)

    return lambda: (
        (cv2.getTrackbarPos("Lower Hue", "Adjust HSV Thresholds"),
         cv2.getTrackbarPos("Lower Saturation", "Adjust HSV Thresholds"),
         cv2.getTrackbarPos("Lower Value", "Adjust HSV Thresholds")),
        (cv2.getTrackbarPos("Upper Hue", "Adjust HSV Thresholds"),
         cv2.getTrackbarPos("Upper Saturation", "Adjust HSV Thresholds"),
         cv2.getTrackbarPos("Upper Value", "Adjust HSV Thresholds"))
    )
