# Extractor
## Using OCR and Translator

## Features

- Extract text from images or documents using Azure Cognitive Services OCR.
- Translate extracted text to multiple languages with the Azure Translator.
- Supports various image formats, including JPEG, PNG, and PDF.
- User-friendly interface for easy image upload and webcam capture.
- Seamless integration with Streamlit for interactive usage.

## Project Details

- [Project Demo Link Here](https://extractor9000.azurewebsites.net/)
- [Project Video Tutorial Link](https://youtu.be/8e5KH-evehA?si=MgMF7nG8-wq4PX1n)

## Azure Service

This project utilizes the following Azure Cognitive Services:

- **Computer Vision OCR API**: To perform optical character recognition and extract text from images or documents.
- **Translator API**: To provide translation services for the extracted text to multiple languages.
- **App Services**: To host the streamlit on azure portal.

## Python Package

The project uses the following Python libraries:

- `azure-cognitiveservices-vision-computervision`: Python SDK for Azure Computer Vision.
- `requests`: For making HTTP requests to the Azure Translator API.
- `streamlit`: For creating the user interface and interactive web app.
- `opencv-python`: For capturing and processing images from the webcam.
- `#created/requirements.txt`

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run main_script.py
```

4. Select the capture method (webcam or upload image) and follow the on-screen instructions to extract and translate text.

## Screenshots

![Screenshot 1](https://github.com/sho6000/Extractor/blob/main/screenshots/1.jpg)

![Screenshot 2](https://github.com/sho6000/Extractor/blob/main/screenshots/2.png)
---
