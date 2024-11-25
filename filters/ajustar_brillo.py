import numpy as np


def ajustar_brillo(frame, factor=1.0):
    """
    Adjusts the brightness of a video frame or image.
    Args:
        frame (numpy.ndarray): The input frame (BGR format).
        factor (float): Brightness adjustment factor (>1 increases brightness, <1 decreases brightness).
    Returns:
        numpy.ndarray: Frame with adjusted brightness.
    """
    if not isinstance(frame, np.ndarray):
        raise ValueError("Input frame must be a numpy.ndarray")

    # Convert frame to float32 to avoid overflow/underflow
    frame_float = frame.astype(np.float32)

    # Scale brightness
    frame_bright = frame_float * factor

    # Clip values to valid range [0, 255] and convert back to uint8
    frame_bright = np.clip(frame_bright, 0, 255).astype(np.uint8)

    return frame_bright
