import cv2


def overlay_image(frame, overlay, x, y, w, h):
    """
    Overlay an image on the frame at the specified position.
    Args:
        frame (numpy.ndarray): The input frame.
        overlay (numpy.ndarray): The overlay image (with alpha channel).
        x, y, w, h: Position and size of the overlay.
    """
    overlay_resized = cv2.resize(overlay, (w, h))
    alpha_overlay = overlay_resized[:, :, 3] / 255.0  # Extract alpha channel
    alpha_background = 1.0 - alpha_overlay

    for c in range(0, 3):  # Loop over color channels
        frame[y:y + h, x:x + w, c] = (
                alpha_overlay * overlay_resized[:, :, c] +
                alpha_background * frame[y:y + h, x:x + w, c]
        )
    return frame
