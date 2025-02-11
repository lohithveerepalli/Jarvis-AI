# Jarvis AI – Siri-Powered AI Assistant with Ollama

## Overview
Jarvis AI transforms Siri into a powerful AI assistant using open-source models like LLaMA. This project enables real-time AI responses through FastAPI and Ollama, ensuring a seamless, local, and private AI experience.

## Features
- Fully offline functionality with open-source models, eliminating API costs.
- Real-time streaming for smooth conversational responses.
- Dynamic question handling without predefined inputs.
- Compatible with macOS and Linux.
- Simple Apple Shortcut integration for easy Siri interaction.

## Installation

### 1. Install Ollama
Ollama is required to run the AI model locally.

For macOS and Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Download the LLaMA model:
```bash
ollama pull llama3.2:1b
```

### 2. Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Jarvis-AI.git
cd Jarvis-AI
```

### 3. Install Dependencies
Create a virtual environment and install required packages:
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r src/requirements.txt
```

### 4. Start the AI Server
Run FastAPI to serve AI responses:
```bash
uvicorn src.ai_api:app --host 0.0.0.0 --port 8080 --workers 1
```
If successful, the output should confirm that Uvicorn is running.

## Setting Up Siri Shortcut

### 1. Import the Shortcut
- Download `Jarvis.shortcut` from the `shortcuts` directory.
- Open the file on an iPhone and install it.

### 2. Configure API URL
- Locate "Get Contents of URL" in the shortcut.
- Replace `http://0.0.0.0:8080/ask` with the local IP of your Mac, for example:
  ```bash
  ipconfig getifaddr en0  # macOS
  hostname -I  # Linux
  ```

### 3. Rename Shortcut to "Jarvis"
- Open the Shortcuts App.
- Rename the shortcut to "Jarvis" to enable activation via voice command.

## Usage
1. Activate Siri and say: "Hey Siri, Jarvis."
2. Ask a question.
3. Siri retrieves and speaks the AI-generated response.

## Troubleshooting

### Siri Does Not Respond
- Ensure the FastAPI server is running:
  ```bash
  curl -X POST "http://YOUR_MAC_IP:8080/ask" -H "Content-Type: application/json" -d '{"prompt": "Hello!"}'
  ```
- Verify that the Mac firewall is not blocking requests:
  ```bash
  sudo pfctl -d  # Temporarily disable the firewall
  ```
- Confirm that both the Mac and iPhone are connected to the same WiFi network.

## Contributing
Contributions are welcome. Fork the repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

