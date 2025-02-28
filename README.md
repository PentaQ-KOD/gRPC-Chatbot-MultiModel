# gRPC Chatbot Multi-Model

This is a chatbot system that integrates multiple models using gRPC for communication. The system can handle text generation and streaming using models like Gemini and Calculator, with the ability to delete models and manage sessions. The project is designed to facilitate interaction with large language models (LLMs) in a conversational manner.

## Features

- **Multiple Models**: Supports multiple models (e.g., Gemini, Calculator) to generate responses.
- **Text Generation**: Generate text responses using the LLMs.
- **Text Streaming**: Stream responses from the LLMs in real-time.
- **Session Management**: Manage chatbot sessions and maintain chat history.
- **Model Management**: Add or delete models for interactions.

## Installation

### Prerequisites

- Python 3.x
- Install required dependencies.

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/PentaQ-KOD/gRPC-Chatbot-MultiModel.git
   cd gRPC-Chatbot-MultiModel
   
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   # On Windows use
   `venv\Scripts\activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

**Usage**
*Starting the gRPC Server*
Start the server by running:
```bash
python gRPC_server.py
```

*Running the Client*
```bash
streamlit run gRPC_client.py
```
On the web interface, you can:

Select an agent (e.g., Gemini).
Input text and choose the response type (Text Generation or Streaming).
Manage your session history.
Delete agents when needed.

**Example**
Here is an example of how to interact with the system:
1. Start the gRPC server (server.py).
2. Open the web interface (client.py via Streamlit).
3. Select the agent (e.g., "Gemini").
4. Input a query, and receive the generated response.

**Contributing**
Feel free to fork this project and submit issues or pull requests. Contributions are welcome!

**Licens**
This project is licensed under the MIT License.





