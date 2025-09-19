import cv2
import numpy as np


def sharpen_image(image):
    """
    Sharpen an image using a convolution kernel.
    
    Args:
        image: Input image
    
    Returns:
        Sharpened image
    """
    if image is None:
        raise ValueError("Input image cannot be None")
    
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened
