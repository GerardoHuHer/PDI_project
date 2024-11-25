import cv2
import numpy as np


def adjust_hue(frame, hue_shift=0):
    """
    Adjust the hue of the frame.
    Args:
        frame (numpy.ndarray): The input video frame (BGR format).
        hue_shift (int): Amount to shift the hue (0-179).
    Returns:
        numpy.ndarray: Frame with adjusted hue.
    """
    if not isinstance(frame, np.ndarray):
        raise ValueError("Input frame must be a numpy.ndarray")

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Adjust the hue channel
    hsv[:, :, 0] = (hsv[:, :, 0] + hue_shift) % 180

    # Convert back to BGR color space
    adjusted_frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return adjusted_frame
