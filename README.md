gRPC Chatbot Multi-Model
This is a chatbot system that integrates multiple models using gRPC for communication. The system can handle text generation and streaming using models like Gemini and Calculator, with the ability to delete models and manage sessions. The project is designed to facilitate interaction with large language models (LLMs) in a conversational manner.

Features
Multiple Models: Supports multiple models (e.g., Gemini, Calculator) to generate responses.
Text Generation: Generate text responses using the LLMs.
Text Streaming: Stream responses from the LLMs in real-time.
Session Management: Manage chatbot sessions and maintain chat history.
Model Management: Add or delete models for interactions.
Installation
Prerequisites
Python 3.x
Install required dependencies.
Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/PentaQ-KOD/gRPC-Chatbot-MultiModel.git
cd gRPC-Chatbot-MultiModel
Create and activate a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
(Optional) If you want to use a specific model, ensure that it is properly configured in the project settings.

Usage
Starting the gRPC Server
Start the server by running:
bash
Copy
Edit
python server.py
Running the Client
To interact with the chatbot, use the client.py script. You can set up a simple Streamlit interface for easy interaction.

bash
Copy
Edit
streamlit run client.py
On the web interface, you can:

Select an agent (e.g., Gemini).
Input text and choose the response type (Text Generation or Streaming).
Manage your session history.
Delete agents when needed.
Configuration
You can modify the settings in the client.py to change the agent and other configurations based on your needs.

Example
Here is an example of how to interact with the system:

Start the gRPC server (server.py).
Open the web interface (client.py via Streamlit).
Select the agent (e.g., "Gemini").
Input a query, and receive the generated response.
Dependencies
grpcio
streamlit
protobuf
requests
sentence-transformers
pymongo
(and any additional dependencies mentioned in the requirements.txt)
Contributing
Feel free to fork this project and submit issues or pull requests. Contributions are welcome!

License
This project is licensed under the MIT License.
