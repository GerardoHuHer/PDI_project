import cv2
import numpy as np


def tophat(frame, kernel_size=15):
    """
    Apply Top-Hat filtering to highlight bright regions in the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
        kernel_size (int): Size of the structuring element.
    Returns:
        numpy.ndarray: Frame with bright regions highlighted.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    tophat_result = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    return cv2.cvtColor(tophat_result, cv2.COLOR_GRAY2BGR)  # Convert back to BGR
