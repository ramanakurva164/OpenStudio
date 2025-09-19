import cv2
import numpy as np
from flip import flip_image
from rotate import rotate_image
from crop import crop_image
from filter import black_and_white_image
from blur import blur_image
from sharpen import sharpen_image
import streamlit as st
from io import BytesIO
from PIL import Image


def convert_image_for_download(image, is_grayscale=False):
    """Convert OpenCV image to downloadable format"""
    if is_grayscale:
        # For grayscale images
        pil_image = Image.fromarray(image)
    else:
        # Convert BGR to RGB for color images
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)
    
    img_buffer = BytesIO()
    pil_image.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    return img_buffer


def main():
    # Load an image
    st.title("OpenCV Image Processing App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Uploaded Image', use_container_width=True)

        task = st.selectbox(
            "Select a task",
            ("Flip", "Rotate", "Crop", "Black and White", "Blur", "Sharpen")
        )

        if task == "Flip":
            direction = st.selectbox("Direction", ("horizontal", "vertical"))
            if st.button("Apply"):
                result = flip_image(image, direction)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption='Flipped Image')
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="Download Flipped Image",
                    data=img_buffer,
                    file_name=f"flipped_{direction}.png",
                    mime="image/png"
                )
                
        elif task == "Rotate":
            angle = st.slider("Angle", 0, 360, 45)
            if st.button("Apply"):
                result = rotate_image(image, angle)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption='Rotated Image')
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="Download Rotated Image",
                    data=img_buffer,
                    file_name=f"rotated_{angle}deg.png",
                    mime="image/png"
                )
                
        elif task == "Crop":
            h, w = image.shape[:2]
            x = st.slider("x", 0, w-1, 50)
            y = st.slider("y", 0, h-1, 50)
            width = st.slider("width", 1, w-x, 200)
            height = st.slider("height", 1, h-y, 200)
            if st.button("Apply"):
                result = crop_image(image, x, y, width, height)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption='Cropped Image')
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="Download Cropped Image",
                    data=img_buffer,
                    file_name=f"cropped_{x}_{y}_{width}x{height}.png",
                    mime="image/png"
                )
                
        elif task == "Black and White":
            if st.button("Apply"):
                result = black_and_white_image(image)
                st.image(result, caption='Black and White Image')
                
                # Download button for grayscale image
                img_buffer = convert_image_for_download(result, is_grayscale=True)
                st.download_button(
                    label="Download Black and White Image",
                    data=img_buffer,
                    file_name="black_and_white.png",
                    mime="image/png"
                )
                
        elif task == "Blur":
            if st.button("Apply"):
                result = blur_image(image)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption='Blurred Image')
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="Download Blurred Image",
                    data=img_buffer,
                    file_name="blurred.png",
                    mime="image/png"
                )
                
        elif task == "Sharpen":
            if st.button("Apply"):
                result = sharpen_image(image)
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption='Sharpened Image')
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="Download Sharpened Image",
                    data=img_buffer,
                    file_name="sharpened.png",
                    mime="image/png"
                )
    else:
        st.info("Please upload an image to get started.")

if __name__ == "__main__":
    main()