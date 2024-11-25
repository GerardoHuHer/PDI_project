import cv2
import numpy as np


def blackhat(frame, kernel_size=15):
    """
    Apply Blackhat morphological operation to highlight dark regions.
    Args:
        frame (numpy.ndarray): The input video frame.
        kernel_size (int): Size of the structuring element.
    Returns:
        numpy.ndarray: Frame with dark regions highlighted.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    blackhat_result = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
    return cv2.cvtColor(blackhat_result, cv2.COLOR_GRAY2BGR)
