# Metadata-Driven AI Workflow Assistant

## Overview
This repository contains the implementation of a **Metadata-Driven AI Workflow Assistant**, designed to help users clarify goals, decompose tasks, discover suitable agents, and generate actionable workflows based on metadata-driven insights.

The assistant leverages OpenAI's advanced capabilities to provide interactive and structured assistance. The application is built using **Streamlit** for a seamless user interface and connects to an OpenAI-powered backend for agent discovery and workflow generation.

---

## Features

1. **Interactive Goal Clarification**: 
   - Engages users with targeted questions to refine their objectives.
   - Leverages metadata from vector databases to guide interactions.

2. **Actionable Task Decomposition**:
   - Breaks down goals into step-by-step workflows.
   - Presents multiple paths with pros and cons for decision-making.

3. **Agent Discovery**:
   - Filters agents from a vector database using metadata fields like category, pricing, and features.
   - Suggests agents tailored to each workflow step.

4. **Workflow Generation**:
   - Generates structured workflows with detailed pros, cons, and agent recommendations.
   - Outputs workflows in both natural language and JSON formats.

5. **User-Centric Design**:
   - Iteratively refines workflows and agent suggestions based on user feedback.

---

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Agent-Workflow-Assistant.git
   cd metadata-ai-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.streamlit/secrets.toml` file with the following content:
     ```toml
     OPENAI_API_KEY = "your-openai-api-key"
     ASST_ID = "your-assistant-id"
     VECTOR_STORE_ID = "your-vector-store-id"
     ```

---

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run streamlit_app.py
   ```

2. Interact with the assistant via the chat interface to:
   - Clarify your goals.
   - Receive workflow suggestions.
   - Discover metadata-driven agents for task automation.

---

## File Structure

```
Agent-Workflow-Assistant/
├── requirements.txt         # Dependencies for the project
├── streamlit_app.py         # Main Streamlit application file
└── .streamlit/
    └── secrets.toml         # Configuration file for API keys and IDs
```

---

## Key Components

### `requirements.txt`
Lists the required Python libraries for the application:
```txt
openai
streamlit
```

### `streamlit_app.py`
Contains the Streamlit application logic, including:
- Initialization of OpenAI client and assistant.
- Management of chat threads and user interactions.
- Execution of assistant workflows using metadata.

### `.streamlit/secrets.toml`
Holds sensitive API keys and identifiers for connecting to the OpenAI API and vector store.

---
