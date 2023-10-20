# Extractor

## Features

- Extract text from images or documents using Azure AI Computer Vision.
- Translate extracted English text to multiple languages with the Azure AI Translator.
- Supports various image formats, including JPEG, PNG, and PDF.
- User-friendly interface for easy image upload and documents.
- Seamless integration with Streamlit for interactive usage.

## Project Details

- [Project Demo Link Here](https://extractor9000.azurewebsites.net/)
- [Project Video Tutorial Link](https://youtu.be/bao-gvTKyGc?si=9KZ_3fMeWG69SUF3)

## Azure Services Used

&rarr;This project utilizes a total of **three Azure Technologies** which are 
- Azure AI Services | Computer Vision
- Azure AI Services | Translator
- Azure App Service

&rarr;Brief Description on the Services Used:
* **Azure AI Services**
  * **Azure AI Translator**: To provide translation services for the extracted text to multiple languages.
  * **Azure Computer Vision**: To perform optical character recognition(OCR) and extract text from images or documents.
* **Azure App Service**: To host the streamlit on Azure portal.

![Screenshot 2023-10-20 004332](https://github.com/sho6000/Extractor/assets/57789899/88af003a-6551-4bd5-ae04-b6523e8f55a3)
---
### Azure AI Services | Computer Vision
- In this project, this service is employed to perform character extraction on images(PNG, JPEG). It can effortlessly extract text from the mentioned and even PDF files. With its robust capabilities, it's an essential component for extracting text from scanned documents or images and making it available for further processing within your application.
- It takes in any type of document or images written in English and is sent to the service to extract data from it
- Inside Computer Vision Studio under the Optical Character Recognition , the feature Extract Text from Image is used to do the work of getting any complicated written text from the different formates.
![Screenshot 2023-10-20 235851](https://github.com/sho6000/Extractor/assets/122631521/155ba48c-6f29-4bfe-be7b-d458e617c2fa)


- The given image below is the example of an extracted text from a pdf file into a json format
![Screenshot 2023-10-21 001322](https://github.com/sho6000/Extractor/assets/122631521/4f78e975-32ee-4a5b-8d03-d839f4e4a6b8)
![Screenshot 2023-10-21 000643](https://github.com/sho6000/Extractor/assets/122631521/9d00f13c-4196-422b-8d17-e804d6f9c6ab)


- After the text is extracted it sent one by one inside a for-loop to the Azure Translator API.
- Below given is the Azure postal under Computer Vision:
![Screenshot 2023-10-20 004839](https://github.com/sho6000/Extractor/assets/57789899/1dc11a05-88ed-404a-8a00-5e5d07c5c861)
![Screenshot 2023-10-20 004646](https://github.com/sho6000/Extractor/assets/57789899/aeae7727-2bf6-4c09-a95a-f09c70abdb20)

---
### Azure AI Services | Translator
- This Azure Service plays a crucial role in making the application multilingual and accessible to a global audience. This service is used to translate the extracted English text into multiple languages. It enables the application to break language barriers, providing seamless communication and understanding for users regardless of their language preferences. This feature is especially valuable in applications where content needs to be translated or localized, broadening the reach and impact of your project.

- In this the extracted text is sent and then each line-by-line is translated from English to any preferred language provided in the application.

- Below given image is an example of the translated English text into "Spanish" and like-wise the user can translated into any desired language from English to any language. This is the translated language from the previous previous example in a JSON format.
![Screenshot 2023-10-21 000717](https://github.com/sho6000/Extractor/assets/122631521/f4767cb9-5d94-4442-8a11-8fd1668c8fed)
- Below given is the Azure postal under Translator:

![Screenshot 2023-10-20 004813](https://github.com/sho6000/Extractor/assets/57789899/9d46453f-0e3f-45e1-ae9e-def553f3e60a)
![Screenshot 2023-10-20 004813](https://github.com/sho6000/Extractor/assets/57789899/911a7548-4248-496c-aef1-ab13f9b7d8e3)

---
### Azure App Service
- Azure App Service serves as the hosting platform for the application's user interface. With this service, I can deploy my application in a convenient and scalable manner. It allows me to focus on the development of my application without the need to manage the underlying infrastructure. This simplifies the deployment process and ensures that the application is easily accessible to users via the Azure portal. Azure App Service provides a robust and reliable environment for your Streamlit-based application, making it available to a broad audience.

- The entire code related from extraction, translations to Streamlit(web-application) is pushed to the Github.
- After the code is pushed successfully, the github project URL is then given to the Azure App service and then the deployment starts automatically.
- Below is the deployment status of the website.
![Screenshot 2023-10-21 002809](https://github.com/sho6000/Extractor/assets/122631521/6fa8a094-d682-4c74-aec2-7929e770d441)
- Below given is the Azure postal under App Service:

![Screenshot 2023-10-20 004919](https://github.com/sho6000/Extractor/assets/57789899/5543d46d-0074-4ff3-83df-622da778072d)
---

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
---

## Steps to Use
- First  we select any image or PDF to upload by clicking on the **Browse files** button.
![Screenshot 2023-10-20 012629](https://github.com/sho6000/sho6000/assets/57789899/bb8624b5-a4b6-4300-9e5a-bcba3bb02adf)
---
- After the the file is selected then the **Azure AI Computer Vision** processes and then a extracted text is displayed below.
![Note](https://github.com/sho6000/Extractor/assets/122631521/2f4e3c8c-ba31-40a2-881c-ba1d471e553b)
---
- **This is the extracted text from the above image:**
![Screenshot 2023-10-21 004420](https://github.com/sho6000/Extractor/assets/122631521/48ae59b9-f9dc-4411-9ef5-9d6ed849273f)
---
- Then we go down and select the preferred language you want to translate.
- Once that is selected the **Azure AI Translator API** translates and displays the text below.
- **In this example I have chosen Arabic:**
![Screenshot 2023-10-21 004641](https://github.com/sho6000/Extractor/assets/122631521/0cf753fa-2358-4609-a42f-7d68c4be260d)
---


## Screenshots

![Screenshot 2023-10-21 004839](https://github.com/sho6000/Extractor/assets/122631521/4586f45c-7d1f-41d4-bb91-0de322e5d442)

![Screenshot 2023-10-21 004815](https://github.com/sho6000/Extractor/assets/122631521/c865ee66-c2ab-426b-b39a-76fbd633ae4e)


