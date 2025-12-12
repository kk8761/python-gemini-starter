# python-gemini-starter
# Gemini AI Agent with Function Calling 🤖

A Python-based AI agent powered by Google's **Gemini 2.0 Flash** model. This project demonstrates how to build an Agentic Workflow using the `google-generativeai` library.

Unlike a standard chatbot, this agent has access to **tools**. It can recognize when a user asks for a calculation, pause the conversation, execute a Python function (like a calculator), and return the mathematically precise result.

## 🚀 Features
* **Gemini Powered:** Uses the latest `gemini-flash-latest` model for high speed and low latency.
* **Function Calling:** The AI can "use hands" to perform actions rather than just guessing text.
* **Math Tools:** Includes custom Python functions for `multiply` and `add` that the AI calls autonomously.
* **Secure:** API Keys are handled safely via environment variables or user input (never hardcoded).

## 🛠️ Prerequisites
* Python 3.9 or higher
* A Google AI Studio API Key (Get one [here](https://aistudio.google.com/))

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/gemini-ai-agent.git](https://github.com/YOUR_USERNAME/gemini-ai-agent.git)
    cd gemini-ai-agent
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

1.  **Run the agent**
    ```bash
    python agent.py
    ```

2.  **Enter your API Key**
    When prompted, paste your Google API Key (input is hidden or secure).

3.  **Chat and Test Math**
    Try asking complex math questions to see the tool usage in action.

    **Example:**
    > **You:** Calculate 342 times 91.
    >
    > **[SYSTEM]** ⚙️ Executing Math: 342.0 * 91.0 ...
    >
    > **Agent:** The result is 31,122.

## 📂 Project Structure
* `agent.py` - The main logic containing the model connection and tool definitions.
* `requirements.txt` - List of necessary Python libraries.

## 🤝 Contributing
Feel free to fork this project and add new tools! You could add:
* Web Search capabilities
* File management tools
* Data visualization tools

## 📝 License
This project is open source and available under the [MIT License](LICENSE).

git add README.md
git commit -m "Add documentation"
git push
