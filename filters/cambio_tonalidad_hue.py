import cv2
import numpy as np


def adjust_hue(frame, hue_shift=0):
    """
    Adjust the hue of the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
        hue_shift (int): Amount to shift the hue (0-179).
    Returns:
        numpy.ndarray: Frame with adjusted hue.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[:, :, 0] = (hsv[:, :, 0] + hue_shift) % 180  # Hue channel shift
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
