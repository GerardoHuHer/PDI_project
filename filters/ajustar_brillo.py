import cv2
import numpy as np


def ajustar_brillo(frame, factor=1.0):
    """
    Adjusts the brightness of a video frame in real-time.
    Args:
        frame (numpy.ndarray): The input video frame.
        factor (float): Brightness adjustment factor (>1 increases brightness, <1 decreases it).
    Returns:
        numpy.ndarray: Frame with adjusted brightness.
    """
    # Convert the frame to float32 to prevent overflow during scaling
    frame = frame.astype(np.float32)

    # Scale each channel by the brightness factor
    frame = frame * factor

    # Clip the values to the valid range [0, 255] and convert back to uint8
    frame = np.clip(frame, 0, 255).astype(np.uint8)

    return frame
