import streamlit as st

import requests
from azure_ocr import GetTextRead
from azure_translator import translate_text
from dotenv import load_dotenv
import os
import numpy as np


# Set the title of the tab
st.set_page_config(page_title="Extraction Application")

# Custom CSS style
cus_css = """
    body {
        color: white; /* Change the text color to white */
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
        background-color: #f2f2f2;
        background-image: repeating-linear-gradient(45deg, transparent, transparent 20px, #c0c0c0 20px, #c0c0c0 40px);
    }
    .stButton {
        background-color: #007BFF !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 5px !important;
    }
    .stSelectbox {
        background-color: #fff !important;
        color: #333 !important;
        font-weight: bold !important;
        border-radius: 5px !important;
    }
    [data-testid="stAppViewContainer"] {
    background-color: #494f00;
opacity: 0.9;
background-image:  linear-gradient(30deg, #000000 12%, transparent 12.5%, transparent 87%, #000000 87.5%, #000000), linear-gradient(150deg, #000000 12%, transparent 12.5%, transparent 87%, #000000 87.5%, #000000), linear-gradient(30deg, #000000 12%, transparent 12.5%, transparent 87%, #000000 87.5%, #000000), linear-gradient(150deg, #000000 12%, transparent 12.5%, transparent 87%, #000000 87.5%, #000000), linear-gradient(60deg, #00000077 25%, transparent 25.5%, transparent 75%, #00000077 75%, #00000077), linear-gradient(60deg, #00000077 25%, transparent 25.5%, transparent 75%, #00000077 75%, #00000077);
background-size: 80px 140px;
background-position: 0 0, 0 0, 40px 70px, 40px 70px, 0 0, 40px 70px;}
    """
# Load environment variables from .env file
load_dotenv()

# Apply custom CSS
st.markdown(f"<style>{cus_css}</style>", unsafe_allow_html=True)

trans_api_key = os.getenv("TRANSLATOR_API_KEY")
trans_api_region = os.getenv("TRANSLATOR_API_REGION")

# Streamlit app title and instructions
st.title("Extractor Application")    

# First field for image upload
st.subheader("Upload your files here")
uploaded_file = st.file_uploader("OCR & Translator from Azure Cognitive Services", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    # Save the uploaded image to a temporary file
    image_path = "temp_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

# Process the image if available
if "image_path" in locals():
    # Call the OCR function and get the extracted text
    uf = image_path
    extracted_text = GetTextRead(uf)

    # Delete the temporary image file
    #os.remove(image_path)
    # Display the extracted text
    if extracted_text:
        st.subheader("Extracted Text:")
        #st.write(extracted_text)
        lines = extracted_text.split("\n")
        for line in lines:
            st.write(line)
        print(lines)
        
        # Dictionary mapping language codes to full names
        language_names = {
            "en": "English",
            "fr": "French",
            "zu": "Zulu",
            "es": "Spanish",
            "it": "Italian",
            "ar": "Arabic",
            "hi": "Hindi",
            "ml": "Malayalam",
            "zh-Hans": "Simplified Chinese",
            "de": "German",
            "ja": "Japanese",
            "ko": "Korean",
            "ru": "Russian",
            "pt": "Portuguese",
            "tr": "Turkish",
            "nl": "Dutch",
            "th": "Thai",
            "sv": "Swedish",
            "fi": "Finnish",
            "no": "Norwegian",
            "da": "Danish",
            "pl": "Polish",
            "id": "Indonesian",
            "uk": "Ukrainian",
            "cs": "Czech",
            "el": "Greek",
            "ro": "Romanian",
            "hu": "Hungarian",
            "he": "Hebrew",
            "bn": "Bengali",
            "ta": "Tamil",
            "te": "Telugu",
            "vi": "Vietnamese",
            "mr": "Marathi",
            "ur": "Urdu", 
            "fa": "Persian",
            "af": "Afrikaans",
            "sw": "Swahili",
            "tl": "Tagalog",
            "ne": "Nepali",
            "pa": "Punjabi",
            "gu": "Gujarati",
            "my": "Burmese",
            "sd": "Sindhi",
            "ha": "Hausa",
            "yo": "Yoruba",
            "ig": "Igbo",
            "si": "Sinhala",
            "km": "Khmer",
            "sn": "Shona",
            "so": "Somali",
            "am": "Amharic",
            "jv": "Javanese",
            "rw": "Kinyarwanda",
            "mg": "Malagasy",
            "zu": "Zulu",
}



       # Third field for language selection
        target_languages = list(language_names.keys())  # Use the list of keys from the dictionary
        target_language = st.selectbox("Select target language for translation",[language_names[code] for code in target_languages])
        for code in target_languages:
            if language_names[code]==target_language:
                print(code)

        for k, v in language_names.items():
            if v == target_language:
                target_language_code = k
                print(target_language_code)

        print("Translator API Key:", trans_api_key)
        print("Translator API Region:", trans_api_region)

        with st.spinner("Translating..."):
            translation_response = translate_text(trans_api_key, trans_api_region, extracted_text, [target_language_code])

        if translation_response:
            # Display the translated text
            translated_text = translation_response[0]['translations'][0]['text']
            st.subheader("Translated Text:")
            #st.write(translated_text)
            lines = translated_text.split("\n")
            for line in lines:
                st.write(line)
        else:
            st.error("Translation failed. Please try again later.")
    else:
        st.error("Text extraction failed.")

        
    
