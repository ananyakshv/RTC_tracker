import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the environment variable for the API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Test function to extract ownership details from OCR text
def extract_ownership_data(ocr_text):
    try:
        # Use the Gemini API to process the text
        response = genai.generateContent(
            model="models/gemma-3-4b-it",  # Choose the model you want to use
            prompt=ocr_text,  # Your OCR text as the prompt
        )
        
        # Print the response (to see if ownership data is extracted correctly)
        print("API Response:", response)
        
        # Extract the relevant information (customize this based on your OCR text structure)
        ownership_data = response['text']
        print("Ownership Data:", ownership_data)
        
        return ownership_data

    except Exception as e:
        print(f"Error extracting ownership data: {e}")
        return None

# Example OCR text (replace with actual OCR text from your RTC document)
ocr_text = """
Owner Name: ಮಾಳಮ್ಮ
Father's Name: ಲೇ. ಹನುಮಪ್ಪ
Area: 0.18 acres
Transaction Type: Purchase
Transaction Year: 72/98-09
"""

if __name__ == "__main__":
    ownership_data = extract_ownership_data(ocr_text)
    print(ownership_data)
