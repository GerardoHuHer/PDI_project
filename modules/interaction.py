import cv2
import numpy as np
from modules.filter_registry import filter_registry


def filter_with_parameters_ui():
    """
    Creates a UI for selecting filters and dynamically adjusting their parameters.
    Displays the name of the currently selected filter on the UI.
    Returns:
        tuple: (selected_filter_name, filter_parameters)
    """

    def nothing(x):
        pass

    # Create UI window
    cv2.namedWindow("Filter Selection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Filter Selection", 600, 100)

    # Create trackbar for filter selection
    cv2.createTrackbar("Filter", "Filter Selection", 0, len(filter_registry) - 1, nothing)

    # Add dynamic sliders for common parameters
    cv2.createTrackbar("Param 1", "Filter Selection", 0, 100, nothing)  # Example for threshold1
    cv2.createTrackbar("Param 2", "Filter Selection", 0, 100, nothing)  # Example for threshold2
    cv2.createTrackbar("Kernel Size", "Filter Selection", 1, 20, nothing)  # Example for kernel size

    def get_parameters():
        # Create a blank image for displaying the filter name
        display_frame = np.zeros((100, 600, 3), dtype=np.uint8)

        # Get selected filter
        current_filter_index = cv2.getTrackbarPos("Filter", "Filter Selection")
        selected_filter = list(filter_registry.keys())[current_filter_index]

        # Display the filter name on the "Filter Selection" window
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_color = (255, 255, 255)
        thickness = 2
        position = (10, 50)

        cv2.putText(
            display_frame,
            f"Filter: {selected_filter}",
            position,
            font,
            font_scale,
            font_color,
            thickness,
            cv2.LINE_AA,
        )
        cv2.imshow("Filter Selection", display_frame)

        # Get parameters from sliders
        param1 = cv2.getTrackbarPos("Param 1", "Filter Selection")
        param2 = cv2.getTrackbarPos("Param 2", "Filter Selection")
        kernel_size = cv2.getTrackbarPos("Kernel Size", "Filter Selection")

        # Ensure kernel size is odd for filters like GaussianBlur
        if kernel_size % 2 == 0:
            kernel_size += 1

        # Define parameter dictionary
        filter_params = {
            "threshold1": param1,
            "threshold2": param2,
            "ksize": kernel_size,
        }

        return selected_filter, filter_params

    return get_parameters
