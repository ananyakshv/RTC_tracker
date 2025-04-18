import requests

def detect_year_from_text(text):
    """
    Function to send text to the LLM API and detect the year of the RTC document.
    Returns the detected year.
    """
    url = "LLM_API_URL"  # replace with your actual API URL
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  # replace with your actual API key
    payload = {
        "text": text
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        # Assuming the API returns a year field
        return data.get('year', None)
    else:
        print(f"Error in API request: {response.status_code}")
        return None

def extract_owner_details(text):
    """
    Function to extract owner details from the RTC document using LLM API.
    Returns a list of owners.
    """
    url = "LLM_API_URL"  # replace with your actual API URL
    headers = {"Authorization": "Bearer YOUR_API_KEY"}  # replace with your actual API key
    payload = {
        "text": text
    }
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        # Assuming the API returns an 'owners' list
        return data.get('owners', [])
    else:
        print(f"Error in API request: {response.status_code}")
        return []
