import cv2
import numpy as np


def blur_image(image):
    """Apply Gaussian blur to an image."""
    if image is None:
        raise ValueError("Input image cannot be None")
    
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred