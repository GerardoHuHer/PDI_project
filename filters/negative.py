import cv2
import numpy as np


def negative(frame):
    """
    Apply a negative effect by inverting the colors of the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
    Returns:
        numpy.ndarray: Frame with inverted colors.
    """
    return cv2.bitwise_not(frame)  # Inverts all pixel values
