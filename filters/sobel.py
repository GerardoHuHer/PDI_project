import cv2
import numpy as np


def sobel(frame, direction='x', ksize=3):
    """
    Apply Sobel edge detection to the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
        direction (str): Direction of the gradient ('x' or 'y').
        ksize (int): Kernel size for the Sobel operator.
    Returns:
        numpy.ndarray: Frame with Sobel edges.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    if direction == 'x':
        sobel_edges = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
    elif direction == 'y':
        sobel_edges = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
    else:
        raise ValueError("Direction must be 'x' or 'y'.")

    sobel_edges = cv2.convertScaleAbs(sobel_edges)  # Convert back to 8-bit
    return cv2.cvtColor(sobel_edges, cv2.COLOR_GRAY2BGR)  # Convert back to BGR
