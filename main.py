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
import os


# Custom CSS for Dino Assistant Theme
def apply_custom_theme():
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
        
        /* Main theme colors - Purple and Teal matching the dino */
        :root {
            --dino-purple: #9B6FD8;
            --dino-teal: #6DD7C8;
            --dino-dark: #1E1E1E;
            --dino-light: #F8F4FF;
        }
        
        /* Global styling */
        * {
            font-family: 'Poppins', sans-serif;
        }
        
        /* Header styling */
        .main-header {
            background: linear-gradient(135deg, #9B6FD8 0%, #6DD7C8 100%);
            padding: 2.5rem;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 8px 25px rgba(155, 111, 216, 0.4);
        }
        
        .main-header h1 {
            color: white;
            font-size: 3.5rem;
            margin: 0;
            font-weight: 700;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        }
        
        .main-header p {
            color: white;
            font-size: 1.3rem;
            margin-top: 0.8rem;
            font-weight: 500;
        }
        
        /* Dino assistant box */
        .dino-assistant {
            background: linear-gradient(135deg, #F3EBFF 0%, #E0F7F3 100%);
            border-left: 6px solid #9B6FD8;
            padding: 2rem;
            border-radius: 15px;
            margin: 1.5rem 0;
            box-shadow: 0 4px 15px rgba(155, 111, 216, 0.15);
        }
        
        .dino-assistant h3 {
            color: #7B4FB8;
            margin-top: 0;
            font-size: 1.5rem;
            font-weight: 600;
        }
        
        .dino-assistant p {
            color: #2D2D2D;
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 0;
        }
        .nav_menu{
                color: black;}
        /* Info boxes */
        .info-box {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            margin: 1.5rem 0;
            border: 3px solid #E8DCFF;
            box-shadow: 0 4px 12px rgba(155, 111, 216, 0.15);
        }
        
        .info-box h4 {
            color: #9B6FD8;
            margin-top: 0;
            font-size: 1.4rem;
            font-weight: 600;
        }
        
        .info-box ol, .info-box ul {
            color: #2D2D2D;
        }
        
        /* Feature cards */
        .feature-card {
            background: white;
            padding: 2rem 1.5rem;
            border-radius: 15px;
            text-align: center;
            margin: 1rem 0;
            border: 3px solid #E8DCFF;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(155, 111, 216, 0.1);
        }
        
        .feature-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 8px 25px rgba(155, 111, 216, 0.3);
            border-color: #9B6FD8;
        }
        
        .feature-icon {
            font-size: 3.5rem;
            margin-bottom: 1rem;
        }
        
        .feature-card h4 {
            color: #7B4FB8;
            font-size: 1.3rem;
            font-weight: 600;
            margin: 0.8rem 0;
        }
        
        .feature-card p {
            color: #444;
            font-size: 1rem;
            line-height: 1.5;
            margin: 0;
        }
        
        /* Button styling */
        .stButton>button {
            background: linear-gradient(135deg, #9B6FD8 0%, #6DD7C8 100%);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.75rem 2.5rem;
            font-weight: 600;
            font-size: 1.05rem;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(155, 111, 216, 0.2);
        }
        
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(155, 111, 216, 0.4);
        }
        
        /* Main app background */
        .main {
            background: linear-gradient(180deg, #FFFFFF 0%, #F8F4FF 100%);
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FEFEFF 0%, #F3EBFF 100%);
        }
        
        /* Sidebar radio buttons */
        [data-testid="stSidebar"] .stRadio > label {
            font-weight: 700;
            color: #9B6FD8;
            font-size: 1.15rem;
            padding: 0.5rem 0;
            display: none; /* Hide the label as we'll show it in HTML */
        }
        
        [data-testid="stSidebar"] .stRadio > div {
            gap: 0.8rem;
            display: flex;
            flex-direction: column;
        }
        
        /* Navigation radio button styling */
        [data-testid="stSidebar"] .stRadio > div > label {
            background: white;
            padding: 1.2rem 1.5rem;
            border-radius: 15px;
            border: 3px solid #E8DCFF;
            transition: all 0.3s ease;
            cursor: pointer;
            font-size: 1.15rem;
            font-weight: 600;
            color: #000000 !important;
            box-shadow: 0 2px 6px rgba(155, 111, 216, 0.08);
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }
        
        /* Text inside radio buttons */
        [data-testid="stSidebar"] .stRadio > div > label > div {
            color: #000000 !important;
        }
        
        [data-testid="stSidebar"] .stRadio > div > label > div > div {
            color: #000000 !important;
        }
        
        [data-testid="stSidebar"] .stRadio > div > label:hover {
            background: linear-gradient(135deg, #F8F4FF 0%, #F0FFFE 100%);
            border-color: #9B6FD8;
            transform: translateX(5px);
            box-shadow: 0 4px 12px rgba(155, 111, 216, 0.2);
            color: #000000 !important;
        }
        
        /* Selected radio button */
        [data-testid="stSidebar"] .stRadio > div > label[data-checked="true"] {
            background: linear-gradient(135deg, #9B6FD8 0%, #6DD7C8 100%);
            color: white !important;
            border-color: #9B6FD8;
            font-weight: 700;
            box-shadow: 0 4px 12px rgba(155, 111, 216, 0.3);
        }
        
        /* Text in selected radio button */
        [data-testid="stSidebar"] .stRadio > div > label[data-checked="true"] > div {
            color: white !important;
        }
        
        [data-testid="stSidebar"] .stRadio > div > label[data-checked="true"] > div > div {
            color: white !important;
        }
        
        /* Radio button circle */
        [data-testid="stSidebar"] .stRadio input[type="radio"] {
            accent-color: #9B6FD8;
        }
        
        /* Upload box */
        [data-testid="stFileUploader"] {
            background: white;
            border: 3px dashed #9B6FD8;
            border-radius: 15px;
            padding: 2rem;
            transition: all 0.3s ease;
        }
        
        [data-testid="stFileUploader"]:hover {
            border-color: #6DD7C8;
            background: #F8F4FF;
        }
        
        /* Radio buttons */
        .stRadio > label {
            font-weight: 600;
            color: #9B6FD8;
            font-size: 1.1rem;
        }
        
        /* Selectbox and slider styling */
        .stSelectbox, .stSlider {
            margin: 1.5rem 0;
        }
        
        /* Success message */
        .stSuccess {
            background: linear-gradient(135deg, #D5F5F0 0%, #B8F0E8 100%);
            border-left: 4px solid #6DD7C8;
            border-radius: 10px;
        }
        
        /* Info message */
        .stInfo {
            background: linear-gradient(135deg, #E8DCFF 0%, #D5F5F0 100%);
            border-left: 4px solid #9B6FD8;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)


def show_landing_page():
    """Display the landing page with dino assistant theme"""
    apply_custom_theme()
    
    # Dino welcome section with image (using base64 encoded image)
    dino_image_base64 = """
    data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfQAAAH0CAYAAADL1t+KAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAgAElEQVR4nOzdd3hU1cLF4X1mMpn0QgqhN0FBQEBAQVFBQFAQUEBRFBVFRVFRUVGUFBUVERURFRUVFBUVFRUEVBQUFRVEUERBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQU
    """ # This would be your actual dino image - for now using placeholder
    
    # Hero Section with Dino
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div style="padding: 2rem 0;">
                <h1 style="color: #9B6FD8; font-size: 3.5rem; font-weight: 700; margin-bottom: 1rem;">
                    Welcome to<br/>DinoStudio! 🦕
                </h1>
                <p style="color: #666; font-size: 1.3rem; line-height: 1.8; margin-bottom: 2rem;">
                    Your friendly AI-powered image editing companion. Transform, enhance, and perfect your photos with just a few clicks!
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Display large dino emoji as mascot placeholder
        st.markdown("""
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 15rem; line-height: 1; 
                     filter: drop-shadow(0 10px 30px rgba(155, 111, 216, 0.3));">
                    🦕
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Welcome message from dino assistant
    st.markdown("""
        <div class="dino-assistant">
            <h3>👋 Hi there! I'm Dino, your photo editing assistant!</h3>
            <p>I'm here to help you transform your images with powerful editing tools. 
            Whether you want to flip, rotate, crop, or apply filters, I've got you covered! 
            Let's make your images look amazing together! 🎨✨</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Features section
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
        <h2 style="color: #9B6FD8; text-align: center; font-size: 2.5rem; margin: 2rem 0;">
            ✨ What I Can Do For You
        </h2>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🔄</div>
                <h4>Flip & Rotate</h4>
                <p>Flip images horizontally or vertically, or rotate them to any angle you want!</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">✂️</div>
                <h4>Crop</h4>
                <p>Cut out the perfect section of your image with precision controls!</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🎨</div>
                <h4>Filters</h4>
                <p>Transform your photos with classic black & white filters!</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">🌫️</div>
                <h4>Blur</h4>
                <p>Add a smooth blur effect for artistic or privacy purposes!</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">✨</div>
                <h4>Sharpen</h4>
                <p>Enhance details and make your images crystal clear!</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class="feature-card">
                <div class="feature-icon">💾</div>
                <h4>Download</h4>
                <p>Save your edited images in high quality PNG format!</p>
            </div>
        """, unsafe_allow_html=True)
    
    
    # How to use section
    st.markdown("<br/><br/>", unsafe_allow_html=True)
    st.markdown("""
        <h2 style="color: #9B6FD8; text-align: center; font-size: 2.5rem; margin: 2rem 0;">
            🚀 How to Get Started
        </h2>
    """, unsafe_allow_html=True)
    
    # Step-by-step guide with columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style="text-align: center; padding: 2rem 1rem;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">📁</div>
                <h3 style="color: #9B6FD8; font-weight: 600;">Step 1: Upload</h3>
                <p style="color: #666; font-size: 1.1rem; line-height: 1.6;">
                    Choose an image from your computer (JPG, JPEG, or PNG)
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="text-align: center; padding: 2rem 1rem;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">🎨</div>
                <h3 style="color: #9B6FD8; font-weight: 600;">Step 2: Edit</h3>
                <p style="color: #666; font-size: 1.1rem; line-height: 1.6;">
                    Select a tool and adjust the settings to your liking
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style="text-align: center; padding: 2rem 1rem;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">💾</div>
                <h3 style="color: #9B6FD8; font-weight: 600;">Step 3: Download</h3>
                <p style="color: #666; font-size: 1.1rem; line-height: 1.6;">
                    Save your masterpiece with a single click!
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
        <div class="dino-assistant">
            <h3>🎉 Ready to get started?</h3>
            <p style="font-size: 1.2rem;">
                Click the <strong>"📸 Editor"</strong> option in the sidebar to begin editing your images! 
                I'll be here to guide you every step of the way! 🌟
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    
    # Footer
    st.markdown("<br/><br/>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; padding: 3rem 1rem; 
             background: linear-gradient(135deg, #F8F4FF 0%, #F0FFFE 100%); 
             border-radius: 15px; margin-top: 3rem;">
            <p style="color: #9B6FD8; font-size: 1.2rem; font-weight: 600; margin: 0;">
                🦕 Made with 💜 by DinoStudio
            </p>
            <p style="color: #666; font-size: 1rem; margin-top: 0.5rem;">
                Powered by OpenCV & Streamlit
            </p>
        </div>
    """, unsafe_allow_html=True)


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


def show_editor():
    """Display the image editor interface"""
    apply_custom_theme()
    
    # Header with dino character
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
            <div style="padding: 2rem 0 1rem 0;">
                <h1 style="color: #9B6FD8; font-size: 3rem; font-weight: 700; margin: 0;">
                    🎨 DinoStudio Editor
                </h1>
                <p style="color: #666; font-size: 1.2rem; margin-top: 0.5rem;">
                    Transform Your Images with Ease
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style="text-align: center; padding-top: 1.5rem;">
                <div style="font-size: 5rem;">🦕</div>
            </div>
        """, unsafe_allow_html=True)

    # Dino assistant helper message
    st.markdown("""
        <div class="dino-assistant">
            <h3>🦕 Let's edit your image!</h3>
            <p>Upload an image below, and I'll help you transform it into something amazing!</p>
        </div>
    """, unsafe_allow_html=True)
    
    # File uploader with better styling
    uploaded_file = st.file_uploader(
        "📁 Choose an image to edit", 
        type=["jpg", "jpeg", "png"],
        help="Supported formats: JPG, JPEG, PNG"
    )
    
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        
        # Display uploaded image in a nice container
        st.markdown("#### 🖼️ Original Image")
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption='Your uploaded image', use_container_width=True)
        
        st.markdown("---")
        
        # Tool selection with better organization
        st.markdown("#### 🎨 Choose Your Editing Tool")
        
        task = st.selectbox(
            "Select what you'd like to do:",
            ("Flip", "Rotate", "Crop", "Black and White", "Blur", "Sharpen"),
            help="Pick a tool and adjust the settings below"
        )

        # Tool-specific settings and processing
        st.markdown("---")
        st.markdown("#### ⚙️ Adjust Settings")
        
        if task == "Flip":
            st.markdown("🦕 **Flip your image horizontally or vertically!**")
            direction = st.radio(
                "Choose flip direction:", 
                ("horizontal", "vertical"),
                horizontal=True
            )
            
            col1, col2 = st.columns([1, 4])
            with col1:
                apply_button = st.button("✨ Apply Flip", use_container_width=True)
            
            if apply_button:
                result = flip_image(image, direction)
                st.markdown("---")
                st.markdown("#### 🎉 Result")
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption=f'Flipped {direction}', use_container_width=True)
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="💾 Download Flipped Image",
                    data=img_buffer,
                    file_name=f"dino_flipped_{direction}.png",
                    mime="image/png",
                    use_container_width=True
                )
                st.success("🦕 Your image has been flipped successfully!")
                
        elif task == "Rotate":
            st.markdown("🦕 **Rotate your image to any angle!**")
            angle = st.slider("Select rotation angle (degrees):", 0, 360, 45, 5)
            st.info(f"Current angle: {angle}°")
            
            col1, col2 = st.columns([1, 4])
            with col1:
                apply_button = st.button("✨ Apply Rotation", use_container_width=True)
            
            if apply_button:
                result = rotate_image(image, angle)
                st.markdown("---")
                st.markdown("#### 🎉 Result")
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption=f'Rotated {angle}°', use_container_width=True)
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="💾 Download Rotated Image",
                    data=img_buffer,
                    file_name=f"dino_rotated_{angle}deg.png",
                    mime="image/png",
                    use_container_width=True
                )
                st.success("🦕 Your image has been rotated successfully!")
                
        elif task == "Crop":
            st.markdown("🦕 **Crop your image to the perfect size!**")
            h, w = image.shape[:2]
            
            st.info(f"Original image size: {w} × {h} pixels")
            
            col1, col2 = st.columns(2)
            with col1:
                x = st.slider("Starting X position:", 0, w-1, 50)
                width = st.slider("Crop width:", 1, w-x, min(200, w-x))
            with col2:
                y = st.slider("Starting Y position:", 0, h-1, 50)
                height = st.slider("Crop height:", 1, h-y, min(200, h-y))
            
            col1, col2 = st.columns([1, 4])
            with col1:
                apply_button = st.button("✨ Apply Crop", use_container_width=True)
            
            if apply_button:
                result = crop_image(image, x, y, width, height)
                st.markdown("---")
                st.markdown("#### 🎉 Result")
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption=f'Cropped to {width}×{height}px', use_container_width=True)
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="💾 Download Cropped Image",
                    data=img_buffer,
                    file_name=f"dino_cropped_{width}x{height}.png",
                    mime="image/png",
                    use_container_width=True
                )
                st.success("🦕 Your image has been cropped successfully!")
                
        elif task == "Black and White":
            st.markdown("🦕 **Convert to classic black and white!**")
            st.info("This will create a timeless monochrome version of your image.")
            
            col1, col2 = st.columns([1, 4])
            with col1:
                apply_button = st.button("✨ Apply Filter", use_container_width=True)
            
            if apply_button:
                result = black_and_white_image(image)
                st.markdown("---")
                st.markdown("#### 🎉 Result")
                st.image(result, caption='Black and White', use_container_width=True)
                
                # Download button for grayscale image
                img_buffer = convert_image_for_download(result, is_grayscale=True)
                st.download_button(
                    label="💾 Download B&W Image",
                    data=img_buffer,
                    file_name="dino_black_and_white.png",
                    mime="image/png",
                    use_container_width=True
                )
                st.success("🦕 Your image is now in beautiful black and white!")
                
        elif task == "Blur":
            st.markdown("🦕 **Add a smooth blur effect!**")
            st.info("Perfect for creating artistic effects or softening details.")
            
            col1, col2 = st.columns([1, 4])
            with col1:
                apply_button = st.button("✨ Apply Blur", use_container_width=True)
            
            if apply_button:
                result = blur_image(image)
                st.markdown("---")
                st.markdown("#### 🎉 Result")
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption='Blurred', use_container_width=True)
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="💾 Download Blurred Image",
                    data=img_buffer,
                    file_name="dino_blurred.png",
                    mime="image/png",
                    use_container_width=True
                )
                st.success("🦕 Your image has been beautifully blurred!")
                
        elif task == "Sharpen":
            st.markdown("🦕 **Enhance image sharpness and details!**")
            st.info("Make your image crisp and clear with enhanced edges.")
            
            col1, col2 = st.columns([1, 4])
            with col1:
                apply_button = st.button("✨ Apply Sharpen", use_container_width=True)
            
            if apply_button:
                result = sharpen_image(image)
                st.markdown("---")
                st.markdown("#### 🎉 Result")
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption='Sharpened', use_container_width=True)
                
                # Download button
                img_buffer = convert_image_for_download(result)
                st.download_button(
                    label="💾 Download Sharpened Image",
                    data=img_buffer,
                    file_name="dino_sharpened.png",
                    mime="image/png",
                    use_container_width=True
                )
                st.success("🦕 Your image is now super sharp!")
    
    else:
        st.markdown("""
            <div class="dino-assistant">
                <h3>🦕 Ready to start?</h3>
                <p>Upload an image using the file uploader above to begin editing!</p>
            </div>
        """, unsafe_allow_html=True)


def main():
    """Main application with navigation"""
    # Page configuration
    st.set_page_config(
        page_title="DinoStudio - Image Editor",
        page_icon="🦕",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Sidebar navigation with improved styling
    st.sidebar.markdown("""
        <div style="text-align: center; padding: 2.5rem 1rem; 
             background: linear-gradient(135deg, #9B6FD8 0%, #6DD7C8 100%); 
             border-radius: 20px; margin-bottom: 1.5rem;
             box-shadow: 0 4px 15px rgba(155, 111, 216, 0.3);">
            <div style="font-size: 5rem; margin-bottom: 1rem; 
                 filter: drop-shadow(0 2px 8px rgba(0,0,0,0.2));">🦕</div>
            <h2 style="color: white; margin: 0; font-weight: 700; font-size: 2rem; 
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">DinoStudio</h2>
            <p style="color: rgba(255,255,255,0.95); font-weight: 500; 
                margin-top: 0.5rem; font-size: 1.1rem;">Image Editor</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation menu with better styling
    st.sidebar.markdown("""
        <h3 style="color: #9B6FD8; font-size: 1.3rem; font-weight: 700; 
             margin-bottom: 1rem; padding-left: 0.5rem;">
            📍 Navigation
        </h3>
    """, unsafe_allow_html=True)
    
    page = st.sidebar.radio(
        "nav_menu",
        ["🏠 Home", "📸 Editor"],
        label_visibility="collapsed"
    )
    
    st.sidebar.markdown("<br/>", unsafe_allow_html=True)
    
    # Sidebar info with better design
    st.sidebar.markdown("""
        <div style="padding: 1.8rem; background: white; 
             border-radius: 15px; border: 3px solid #E8DCFF; margin: 1.5rem 0;
             box-shadow: 0 2px 8px rgba(155, 111, 216, 0.1);">
            <h4 style="color: #9B6FD8; margin-top: 0; font-weight: 700; font-size: 1.2rem; 
                 margin-bottom: 1rem;">💡 Quick Tips</h4>
            <ul style="font-size: 1rem; color: #444; line-height: 2; padding-left: 1.5rem; margin: 0;">
                <li><strong>Upload</strong> images up to 200MB</li>
                <li><strong>Supports</strong> JPG, JPEG, PNG</li>
                <li><strong>Local</strong> processing only</li>
                <li><strong>Download</strong> in high quality</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Add a fun dino tip
    st.sidebar.markdown("""
        <div style="padding: 1.8rem; background: linear-gradient(135deg, #F3EBFF 0%, #E0F7F3 100%); 
             border-radius: 15px; border-left: 5px solid #9B6FD8; margin: 1.5rem 0;
             box-shadow: 0 2px 8px rgba(155, 111, 216, 0.1);">
            <h4 style="color: #7B4FB8; margin-top: 0; font-weight: 700; font-size: 1.2rem;
                 margin-bottom: 0.8rem;">🦕 Dino Tip</h4>
            <p style="font-size: 1rem; color: #444; margin: 0; line-height: 1.7;">
                Try different tools to see which effect works best for your image. 
                Don't be afraid to experiment! 🎨
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Footer in sidebar
    st.sidebar.markdown("<br/>", unsafe_allow_html=True)
    st.sidebar.markdown("""
        <div style="text-align: center; padding: 1rem; color: #9B6FD8; 
             font-size: 0.9rem; border-top: 2px solid #E8DCFF; margin-top: 2rem;">
            <p style="margin: 0; font-weight: 600;">Made with 💜</p>
            <p style="margin: 0.3rem 0 0 0; color: #666;">v1.0.0</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Display selected page
    if page == "🏠 Home":
        show_landing_page()
    elif page == "📸 Editor":
        show_editor()


if __name__ == "__main__":
    main()