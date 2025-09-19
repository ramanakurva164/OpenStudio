import cv2
import numpy as np


def flip_image(image, direction='horizontal'):
    """
    Flip an image horizontally or vertically.
    
    Args:
        image: Input image
        direction: 'horizontal' or 'vertical'
    
    Returns:
        Flipped image
    """
    if image is None:
        raise ValueError("Input image cannot be None")
    
    if direction == 'horizontal':
        flipped = cv2.flip(image, 1)
    elif direction == 'vertical':
        flipped = cv2.flip(image, 0)
    else:
        raise ValueError("Direction must be 'horizontal' or 'vertical'")
    return flipped
