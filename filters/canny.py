import cv2


def canny(frame, threshold1=100, threshold2=200):
    """
    Apply Canny edge detection to the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
        threshold1 (int): First threshold for hysteresis.
        threshold2 (int): Second threshold for hysteresis.
    Returns:
        numpy.ndarray: Frame with edges highlighted.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    edges = cv2.Canny(gray, threshold1, threshold2)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)  # Convert back to BGR for compatibility
