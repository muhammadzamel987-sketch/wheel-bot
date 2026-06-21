import google.generativeai as genai

# Paste your API key here to test
genai.configure(api_key="YOUR_ACTUAL_API_KEY_HERE")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Available Model: {m.name}")