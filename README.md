**SimpleChatBot**
=====================

A sandbox repository showcasing different implementations of simple chatbots using LangChain and LangGraph.

**Introduction**
---------------

This repository contains local implementations of chatbots, where each chatbot builds off the other through basic components including prompt templates & short term memory.

**Naive Chat Bot (`naiveChatBot.py`)**
------------------------------------

This is a simple chatbot that uses Ollama as its model, specifically Llama 3.2. It serves as a starting point for understanding how to integrate LangChain with an LLM.

One notable aspect of this implementation is the absence of short-term memory. The chatbot only processes user input and generates responses based on the current context, without retaining any information from previous interactions. This design choice allows for a straightforward demonstration of using Ollama with LangChain.

**Lang Graph Memory Bot (`langGraphMemBot.py`)**
---------------------------------------------

This implementation builds upon the previous one by incorporating short-term memory capabilities. The Lang Graph Memory Bot uses the `langGraph` library to enable context-dependent
responses.

By leveraging Lang Graph's architecture, this chatbot demonstrates a more advanced approach to NLP, where the model can retain information from previous interactions and generate more informed responses.


**Getting Started**
------------------

To replicate this repository, please follow these steps:

### 1. Install Required Dependencies

Create a new virtual environment using `python -m venv myenv` (or your preferred method). Activate the environment: `source myenv/bin/activate` (on Linux/Mac) or
`myenv\Scripts\activate` (on Windows).

Install the required dependencies by running: `pip install -r requirements.txt`

### 2. Download and Install Ollama

Visit the official Llama repository: <https://github.com/facebookresearch/ollama>

Download the pre-trained model for your desired language and architecture.

Follow the instructions in `README.md` to install and configure Ollama.

### 3. Clone this Repository

Fork the SimpleChatBot repository using Git: `git fork https://github.com/[your-username]/SimpleChatBot`

Please note that you'll need to replace `[your-username]` with your actual GitHub username.

**Requirements**
---------------

To run the chatbots, ensure you have Python 3.9+ installed on your system. Additionally, please make sure Ollama is properly installed and configured before proceeding.
