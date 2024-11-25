import cv2
import numpy as np


def pseudocolor(frame):
    """
    Apply pseudocolor mapping to the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
    Returns:
        numpy.ndarray: Frame with pseudocolor applied.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    pseudocolored_frame = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    return pseudocolored_frame
