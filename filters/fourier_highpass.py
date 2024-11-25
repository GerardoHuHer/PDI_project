import cv2
import numpy as np


def fourier_highpass(frame, cutoff=30):
    """
    Apply a high-pass filter in the frequency domain.
    Args:
        frame (numpy.ndarray): The input video frame.
        cutoff (int): Cutoff frequency radius.
    Returns:
        numpy.ndarray: Frame with high-pass filter applied.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    rows, cols = gray.shape
    crow, ccol = rows // 2, cols // 2

    mask = np.ones((rows, cols, 2), np.float32)
    mask[crow - cutoff:crow + cutoff, ccol - cutoff:ccol + cutoff] = 0

    dft_shift = dft_shift * mask
    dft_ishift = np.fft.ifftshift(dft_shift)
    img_back = cv2.idft(dft_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    # Normalize to 8-bit
    normalized = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    return cv2.cvtColor(normalized.astype(np.uint8), cv2.COLOR_GRAY2BGR)
