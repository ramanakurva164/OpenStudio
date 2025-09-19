import cv2
import numpy as np


def black_and_white_image(image):
    """
    Convert a color image to grayscale (black and white).
    
    Args:
        image: Input color image
    
    Returns:
        Grayscale image
    """
    if image is None:
        raise ValueError("Input image cannot be None")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray