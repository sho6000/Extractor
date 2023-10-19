# Extractor

## Features

- Extract text from images or documents using Azure Cognitive Services OCR.
- Translate extracted text to multiple languages with the Azure Translator.
- Supports various image formats, including JPEG, PNG, and PDF.
- User-friendly interface for easy image upload and webcam capture.
- Seamless integration with Streamlit for interactive usage.

## Project Details

- [Project Demo Link Here](https://extractor9000.azurewebsites.net/)
- [Project Video Tutorial Link]()

## Azure Services Used

&rarr;This project utilizes a total of **three Azure Technologies** which are 
- Azure AI Services | Computer Vision
- Azure AI Services | Translator
- Azure App Service

&rarr;Brief Description on the Services Used:
* **Azure AI Services**: Used to do basic operations of the application such as scanning and linguistics.
  * **Azure AI Translator**: To provide translation services for the extracted text to multiple languages.
  * **Azure Computer Vision**: To perform optical character recognition and extract text from images or documents.
* **Azure App Service**: To host the streamlit on Azure portal.

![Screenshot 2023-10-20 004332](https://github.com/sho6000/Extractor/assets/57789899/88af003a-6551-4bd5-ae04-b6523e8f55a3)

### Azure AI Services | Computer Vision
- Azure AI Services | Computer Vision is a powerful tool for image analysis and text extraction. In your project, this service is employed to perform optical character recognition (OCR) on images or documents. It can effortlessly extract text from a variety of image formats, including JPEG, PNG, and even PDF files. With its robust capabilities, it's an essential component for extracting text from scanned documents or images and making it available for further processing within your application.
![Screenshot 2023-10-20 004839](https://github.com/sho6000/Extractor/assets/57789899/1dc11a05-88ed-404a-8a00-5e5d07c5c861)
![Screenshot 2023-10-20 004646](https://github.com/sho6000/Extractor/assets/57789899/aeae7727-2bf6-4c09-a95a-f09c70abdb20)


### Azure AI Services | Translator
- The Azure AI Services | Translator plays a crucial role in making your application multilingual and accessible to a global audience. This service is used to translate the extracted text into multiple languages. It enables your application to break language barriers, providing seamless communication and understanding for users regardless of their language preferences. This feature is especially valuable in applications where content needs to be translated or localized, broadening the reach and impact of your project.
![Screenshot 2023-10-20 004813](https://github.com/sho6000/Extractor/assets/57789899/9d46453f-0e3f-45e1-ae9e-def553f3e60a)
![Screenshot 2023-10-20 004813](https://github.com/sho6000/Extractor/assets/57789899/911a7548-4248-496c-aef1-ab13f9b7d8e3)


### Azure App Service
- Azure App Service serves as the hosting platform for your application's user interface. With this service, you can deploy your application in a convenient and scalable manner. It allows you to focus on the development of your application without the need to manage the underlying infrastructure. This simplifies the deployment process and ensures that your application is easily accessible to users via the Azure portal. Azure App Service provides a robust and reliable environment for your Streamlit-based application, making it available to a broad audience.
![Screenshot 2023-10-20 004919](https://github.com/sho6000/Extractor/assets/57789899/5543d46d-0074-4ff3-83df-622da778072d)


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

![Screenshot 2023-10-20 012629](https://github.com/sho6000/sho6000/assets/57789899/bb8624b5-a4b6-4300-9e5a-bcba3bb02adf)

![2](https://github.com/sho6000/Extractor/assets/57789899/7e4095a0-0e8f-42d1-bffc-56896df64df6)
---
