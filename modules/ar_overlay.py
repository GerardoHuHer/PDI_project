def overlay_multiple_objects(frame, objects, overlay, scale_factor=1.0):
    """
    Overlay an image on multiple detected objects.
    Args:
        frame (numpy.ndarray): The input frame.
        objects (list): List of bounding boxes [(x, y, w, h)].
        overlay (numpy.ndarray): The overlay image (with alpha channel).
        scale_factor (float): Scaling factor for overlay size.
    Returns:
        numpy.ndarray: Frame with overlays applied.
    """
    for (x, y, w, h) in objects:
        resized_overlay = cv2.resize(overlay, (int(w * scale_factor), int(h * scale_factor)))
        frame = overlay_image(frame, resized_overlay, x, y, w, h)
    return frame
