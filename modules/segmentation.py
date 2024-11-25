import cv2
import numpy as np


def segment_by_color(frame, lower_hsv, upper_hsv):
    """
    Segment objects in the frame based on HSV color range.
    Args:
        frame (numpy.ndarray): The input frame.
        lower_hsv (tuple): Lower bound of HSV values.
        upper_hsv (tuple): Upper bound of HSV values.
    Returns:
        numpy.ndarray: The segmented frame.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    segmented = cv2.bitwise_and(frame, frame, mask=mask)
    return segmented
