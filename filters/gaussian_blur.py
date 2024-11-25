import cv2


def gaussian_blur(frame, ksize=15):
    """
    Apply Gaussian blur to the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
        ksize (int): Kernel size for the blur (must be odd).
    Returns:
        numpy.ndarray: Blurred frame.
    """
    return cv2.GaussianBlur(frame, (ksize, ksize), 0)
