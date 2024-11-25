import cv2
import numpy as np


def laplacian_edge(frame):
    """
    Apply Laplacian edge detection to the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
    Returns:
        numpy.ndarray: Frame with Laplacian edges.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)  # Convert back to 8-bit
    return cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR)
