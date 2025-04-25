# utils.py

import google.generativeai as genai

def extract_ownership_from_ocr(ocr_text):
    # Assuming the correct function for text generation is 'generate_text'
    response = genai.generate_text(
        prompt=ocr_text,
        model="text-bison-001",  # Use the correct model name here
        temperature=0.5,  # Adjust based on your needs
        max_output_tokens=1024
    )

    # Assuming the model returns text in the following format
    extracted_text = response.result
    ownership_details = []

    # Example parsing logic - adjust this based on how your model outputs the result
    lines = extracted_text.split("\n")
    name, father_name, area = None, None, None
    
    for line in lines:
        if "Owner" in line:
            if name:  # If name is already captured, store the details
                ownership_details.append({
                    'name': name,
                    'father_name': father_name,
                    'area': area
                })
            name = line.split(":")[1].strip()
        elif "Father" in line:
            father_name = line.split(":")[1].strip()
        elif "Area" in line:
            area = line.split(":")[1].strip()

    if name:  # Append the last extracted owner
        ownership_details.append({
            'name': name,
            'father_name': father_name,
            'area': area
        })

    print(f"Extracted Ownership Details: {ownership_details}")  # Log the result to check

    return ownership_details
