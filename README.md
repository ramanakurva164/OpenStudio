# OpenCV Image Processing App

A powerful web-based image processing application built with Streamlit and OpenCV that allows users to perform various image transformations and filters with an intuitive interface.

## 🚀 Features

- **Image Upload**: Support for JPG, JPEG, and PNG formats
- **Flip Operations**: Horizontal and vertical image flipping
- **Rotation**: Rotate images by any angle (0-360 degrees)
- **Cropping**: Interactive cropping with adjustable dimensions
- **Black & White Filter**: Convert images to grayscale
- **Blur Effect**: Apply blur filter to images
- **Sharpen Filter**: Enhance image sharpness
- **Download Functionality**: Download processed images in PNG format
- **Real-time Preview**: Instant preview of all transformations

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/ramanakurva164/newww.git
cd newww
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Upload an image using the file uploader

4. Select your desired processing operation from the dropdown menu

5. Adjust parameters (if applicable) and click "Apply"

6. Download your processed image using the download button

### Supported Operations

#### Flip
- **Horizontal**: Mirror image left-to-right
- **Vertical**: Mirror image top-to-bottom

#### Rotate
- Rotate image by any angle from 0 to 360 degrees
- Use the slider to select your desired rotation angle

#### Crop
- Interactive cropping with adjustable parameters:
  - X coordinate (starting position)
  - Y coordinate (starting position)
  - Width and Height of the crop area

#### Filters
- **Black and White**: Convert to grayscale
- **Blur**: Apply Gaussian blur effect
- **Sharpen**: Enhance image details and edges

## 📁 Project Structure

```
newww/
├── app.py                 # Main Streamlit application
├── flip.py               # Image flipping functions
├── rotate.py             # Image rotation functions
├── crop.py               # Image cropping functions
├── filter.py             # Black and white filter
├── blur.py               # Blur effect functions
├── sharpen.py            # Sharpening functions
├── requirements.txt      # Python dependencies
```

## 🔧 Dependencies

The application uses the following main libraries:

- **Streamlit** (≥1.30): Web application framework
- **OpenCV** (cv2): Image processing operations
- **NumPy** (≥1.25.0): Numerical operations

## 🎯 Key Functions

### Image Conversion
```python
def convert_image_for_download(image, is_grayscale=False):
    """Convert OpenCV image to downloadable format"""
```

### Main Application
```python
def main():
    """Main Streamlit application function"""
```

## 🚀 Deployment

The application is configured for deployment with:
- `requirements.txt`: Lists all dependencies
- Streamlit-ready configuration

To deploy on platforms like Heroku, Streamlit Cloud, or similar:
1. Ensure all files are in your repository
2. Connect your repository to your deployment platform
3. The platform will automatically use the configuration files

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Author

- **Ramana Kurva** - *Initial work* - [ramanakurva164](https://github.com/ramanakurva164)

## 🙏 Acknowledgments

- OpenCV community for excellent computer vision tools
- Streamlit team for the amazing web app framework
- PIL/Pillow developers for image processing capabilities

## 📞 Support

If you have any questions or need help with this project, please:

- Open an issue on GitHub
- Check the documentation in the `docs/` directory

## 🔄 Version History

### [Version 1.0.0] - 2025-09-19
- Initial release with core image processing features
- Streamlit web interface implementation
- Download functionality for processed images
- Support for multiple image formats

---

⭐ **If you found this project helpful, please give it a star!** ⭐

## 🖼️ Screenshots

Upload your image and start processing immediately with our intuitive interface!

*Note: Add screenshots of your application interface here to showcase the user experience.*
