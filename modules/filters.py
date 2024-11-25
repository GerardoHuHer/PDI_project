import cv2


def apply_filter(frame, filter_type):
    """
    Apply a specified filter to the frame.
    Args:
        frame (numpy.ndarray): The input frame.
        filter_type (str): Type of filter ('blur', 'edges', etc.).
    Returns:
        numpy.ndarray: The filtered frame.
    """
    if filter_type == 'blur':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    elif filter_type == 'edges':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    return frame
