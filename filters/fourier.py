import cv2
import numpy as np


def fourier_transform(frame):
    """
    Apply Fourier Transform to visualize the frequency domain of the image.
    Args:
        frame (numpy.ndarray): The input video frame.
    Returns:
        numpy.ndarray: Frame visualizing the frequency domain.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    # Normalize to 8-bit for visualization
    normalized = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
    return cv2.cvtColor(normalized.astype(np.uint8), cv2.COLOR_GRAY2BGR)
