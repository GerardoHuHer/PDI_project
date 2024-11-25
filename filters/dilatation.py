import cv2
import numpy as np


def dilatation(frame, kernel_size=3):
    """
    Apply dilatation to the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
        kernel_size (int): Size of the structuring element.
    Returns:
        numpy.ndarray: Frame after dilatation.
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    dilated_frame = cv2.dilate(frame, kernel, iterations=1)
    return dilated_frame
