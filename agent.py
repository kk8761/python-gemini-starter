import google.generativeai as genai
import os

# --- 1. SETUP ---
# Paste your API key here (Keep the quotes!)
MY_API_KEY = "Upload your api key here"
genai.configure(api_key=MY_API_KEY)

# --- 2. DEFINE TOOLS ---
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers. Use this for complex math."""
    print(f"\n[SYSTEM] ⚙️ Executing: {a} * {b} ...") 
    return a * b

def add(a: float, b: float) -> float:
    """Adds two numbers."""
    print(f"\n[SYSTEM] ⚙️ Executing: {a} + {b} ...") 
    return a + b

# Create the toolbox
my_toolbox = [multiply, add]

# --- 3. INITIALIZE MODEL ---
print(f"Connecting to Gemini 2.0 Flash...")
# WE ARE USING THE MODEL FOUND IN YOUR LIST:
model = genai.GenerativeModel(
    model_name='gemini-flash-latest', 
    tools=my_toolbox
)
# --- 4. THE CHAT LOOP ---
def chat_with_agent():
    chat = model.start_chat(enable_automatic_function_calling=True)
    
    print("\n------------------------------------------------")
    print("SUCCESS: Gemini 2.0 Agent is online!")
    print("Try asking: 'Calculate 55 times 122'")
    print("------------------------------------------------\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        
        try:
            response = chat.send_message(user_input)
            print(f"Agent: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_agent()