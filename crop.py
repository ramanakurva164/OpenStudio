import cv2
import numpy as np


def crop_image(image, x, y, width, height):
    """
    Crop an image to a specified rectangular region.
    
    Args:
        image: Input image
        x: Starting x coordinate
        y: Starting y coordinate
        width: Width of crop region
        height: Height of crop region
    
    Returns:
        Cropped image
    """
    if image is None:
        raise ValueError("Input image cannot be None")
    
    h, w = image.shape[:2]
    
    # Ensure coordinates are within image bounds
    x = max(0, min(x, w-1))
    y = max(0, min(y, h-1))
    width = max(1, min(width, w-x))
    height = max(1, min(height, h-y))
    
    return image[y:y+height, x:x+width] 