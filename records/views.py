import re
from django.shortcuts import render
from .models import CropSeason, Owner

# Assuming you have an extract_ownership_from_ocr function that works directly with the text
def extract_ownership_from_ocr(ocr_text):
    # Assuming ocr_text has ownership info in the form of a list of owners with their details
    # Extracting data in a list of dictionaries for each owner

    ownership_data = []
    lines = ocr_text.strip().split("\n")

    # Iterate through lines and extract owner details
    owner = {}
    for line in lines:
        if line.startswith("Owner:"):
            if owner:  # If we have a previous owner, add them to the list
                ownership_data.append(owner)
            owner = {"name": line.split(":")[1].strip()}  # Start a new owner
        elif line.startswith("Father Name:"):
            owner["father_name"] = line.split(":")[1].strip()
        elif line.startswith("Area:"):
            owner["area"] = float(line.split(":")[1].strip())
    
    if owner:  # Add the last owner after the loop ends
        ownership_data.append(owner)

    return ownership_data


# views.py

from django.shortcuts import render
from .utils import extract_ownership_from_ocr  # Import the function from utils
from .models import CropSeason

def crop_season_view(request):
    ocr_text = """
    Owner: ಮಾಳಮ್ಮ
    Father Name: ಲೇ. ಹನುಮಪ್ಪ
    Area: 0.18

    Owner: ರಾಜಣ್ಣ
    Father Name: ಪ. ಮುನಿಶಾಮಪ್ಪ
    Area: 0.09

    Owner: ಆಂಜನಪ್ಪ
    Father Name: ಮುನಿಶಾಮಪ್ಪ
    Area: 0.04
    """
    
    ownership_details = extract_ownership_from_ocr(ocr_text)  # Use the function here
    print(f"Ownership Details: {ownership_details}")  # Log to check
    
    crop_seasons = CropSeason.objects.all()  # Fetch crop seasons for display
    
    return render(request, 'records/crop_season.html', {
        'crop_seasons': crop_seasons,
        'ownership_details': ownership_details
    })

def ownership_view(request):
    # Retrieve and display owners from the database
    owners = Owner.objects.all().order_by('transaction_year')
    return render(request, 'records/ownership.html', {'owners': owners})
