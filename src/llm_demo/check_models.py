import google.generativeai as genai

genai.configure(api_key="AIzaSyCvYyWePmmWflfDiqopdSW0_-vbpiTU23w")

for m in genai.list_models():
    print(m.name)
