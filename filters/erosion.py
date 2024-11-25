import cv2
import numpy as np


def erosion(frame, kernel_size=3):
    """
    Apply erosion to the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
        kernel_size (int): Size of the structuring element.
    Returns:
        numpy.ndarray: Frame after erosion.
    """
    if not isinstance(frame, np.ndarray):
        raise ValueError("Input frame must be a numpy.ndarray")

    # Ensure kernel size is odd and positive
    if kernel_size < 1:
        kernel_size = 1
    if kernel_size % 2 == 0:
        kernel_size += 1

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    eroded_frame = cv2.erode(frame, kernel, iterations=1)
    return eroded_frame
