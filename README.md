# 💬 Chatbot

Welcome to the Chatbot application! This application allows users to interact with an AI assistant using a conversational interface powered by the `ollama` library.

## Features

- **Chat Interface**: A simple and intuitive chat interface for interacting with the AI assistant.
- **Message History**: Keeps track of the conversation history between the user and the assistant.
- **Streaming Responses**: Generates and displays responses from the assistant in real-time.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/harshchi19/app.git
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Start the Application**: Run the Streamlit application as described above.
2. **Interact with the Assistant**: Use the chat input box to send messages to the assistant. The assistant's responses will be generated and displayed in real-time.
3. **View Message History**: The conversation history is displayed, showing messages from both the user and the assistant.


#### Key Components:

- **Session State**: Utilizes Streamlit's session state to store and manage the conversation history.
- **Message Display**: Displays the conversation history, distinguishing between user and assistant messages with avatars.
- **Response Generation**: Uses the `ollama` library to generate responses from the assistant. Supports streaming of response tokens for real-time display.

### Dependencies

- `streamlit`
- `ollama`

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- The `ollama` library for powering the conversational AI model.
- Streamlit for providing an easy-to-use framework for creating web applications.

