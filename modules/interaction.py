def handle_keyboard(key, current_filter):
    """
    Handle keyboard input to switch between filters.
    Args:
        key (int): Key pressed.
        current_filter (str): Current filter in use.
    Returns:
        str: Updated filter type.
    """
    if key == ord('b'):  # Blur filter
        return 'blur'
    elif key == ord('e'):  # Edge detection
        return 'edges'
    elif key == ord('n'):  # No filter
        return 'none'
    return current_filter
