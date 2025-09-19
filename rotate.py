import cv2
import numpy as np


def rotate_image(image, angle):
    """
    Rotate an image by a specified angle.
    
    Args:
        image: Input image
        angle: Rotation angle in degrees
    
    Returns:
        Rotated image
    """
    if image is None:
        raise ValueError("Input image cannot be None")
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated
