import google.generativeai as genai

# --- PASTE YOUR KEY BELOW ---
MY_API_KEY = "Upload your API Key here"

genai.configure(api_key=MY_API_KEY)

print("Checking available models for your key...")
try:
    # Ask Google for the list
    for m in genai.list_models():
        # Only show models that can chat/generate text
        if 'generateContent' in m.supported_generation_methods:
            print(f"FOUND: {m.name}")
            
except Exception as e:

    print(f"Error: {e}")
