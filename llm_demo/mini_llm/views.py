
from django.shortcuts import render
from django.conf import settings
import google.generativeai as genai

genai.configure(api_key=settings.GEMINI_API_KEY)

def extract_names_view(request):
    result = ""
    if request.method == "POST":
        input_text = request.POST.get("input_text")

        try:
            model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

            prompt = f"""
            Extract the following structured data from this Kannada land record (RTC) text:

            1. Owner name
            2. Area (in acres or hectares)
            3. Transaction year (e.g., 113/94-95, or 05-11-2008)
            4. Crop Data:
                - Year (e.g., 2013-14)
                - Season (ಮುಂಗಾರ or ಹಿಂಗಾರು)
                - Farmer names involved in that year and season

            Return JSON in the following format:
            {{
              "owners": [
                {{"name": "...", "area": "...", "transaction_year": "..."}},
                ...
              ],
              "crop_seasons": [
                {{"year": "...", "season": "...", "farmers": ["...", "..."]}},
                ...
              ]
            }}

            Text:
            {input_text}
            """

            response = model.generate_content(prompt)
            result = response.text

        except Exception as e:
            result = f"❌ Error: {str(e)}"

    return render(request, "mini_llm/extract_names.html", {"result": result})
