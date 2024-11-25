from filters.ajustar_brillo import ajustar_brillo
from filters.canny import canny
from filters.gaussian_blur import gaussian_blur
from filters.negative import negative
from filters.sobel import sobel
from filters.tophat import tophat
from filters.blackhat import blackhat
from filters.pseudocolor import pseudocolor
from filters.fourier import fourier_transform
from filters.perimeter import perimeter_detection
from filters.laplacian import laplacian_edge
from filters.erosion import erosion
from filters.dilatation import dilatation
from filters.cambio_tonalidad_hue import adjust_hue
from filters.esqueleto import skeletonize
from filters.fourier_highpass import fourier_highpass

# Filter registry
filter_registry = {
    "Ajustar Brillo": ajustar_brillo,
    "Canny Edge Detection": canny,
    "Gaussian Blur": gaussian_blur,
    "Negative (Invert Colors)": negative,
    "Sobel Edge Detection (X)": lambda frame, **kwargs: sobel(frame, direction='x', **kwargs),
    "Sobel Edge Detection (Y)": lambda frame, **kwargs: sobel(frame, direction='y', **kwargs),
    "Top-Hat Filter": tophat,
    "Blackhat Filter": blackhat,
    "Pseudocolor Filter": pseudocolor,
    "Fourier Transform": fourier_transform,
    "Perimeter Detection": perimeter_detection,
    "Laplacian Edge Detection": laplacian_edge,
    "Erosion": erosion,
    "Dilatation": dilatation,
    "Hue Adjustment": adjust_hue,
    "Skeletonization": skeletonize,
    "Fourier High-Pass Filter": fourier_highpass,
}

# Expected parameters for each filter
filter_params_map = {
    "Ajustar Brillo": ["factor"],
    "Canny Edge Detection": ["threshold1", "threshold2"],
    "Gaussian Blur": ["ksize"],
    "Negative (Invert Colors)": [],
    "Sobel Edge Detection (X)": ["ksize"],
    "Sobel Edge Detection (Y)": ["ksize"],
    "Top-Hat Filter": ["kernel_size"],
    "Blackhat Filter": ["kernel_size"],
    "Pseudocolor Filter": [],
    "Fourier Transform": [],
    "Perimeter Detection": ["threshold"],
    "Laplacian Edge Detection": [],
    "Erosion": ["kernel_size"],
    "Dilatation": ["kernel_size"],
    "Hue Adjustment": ["hue_shift"],
    "Skeletonization": [],
    "Fourier High-Pass Filter": ["cutoff"],
}


def apply_filter_by_name(frame, filter_name, **kwargs):
    """
    Apply a filter from the registry by its name.
    Args:
        frame (numpy.ndarray): The input frame.
        filter_name (str): Name of the filter to apply.
        kwargs: Additional parameters for the filter function.
    Returns:
        numpy.ndarray: Processed frame.
    """
    if filter_name in filter_registry:
        # Filter out invalid parameters
        valid_params = filter_params_map.get(filter_name, [])
        filtered_kwargs = {key: kwargs[key] for key in valid_params if key in kwargs}

        # Call the filter function with the valid parameters
        return filter_registry[filter_name](frame, **filtered_kwargs)
    else:
        print(f"Filter '{filter_name}' not found!")
        return frame
