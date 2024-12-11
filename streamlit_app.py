import streamlit as st
from openai import OpenAI
import time

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
ASSISTANT_ID = st.secrets["ASST_ID"]
VECTOR_STORE_ID = st.secrets["VECTOR_STORE_ID"]


client = OpenAI(api_key=OPENAI_API_KEY)

assistant = client.beta.assistants.retrieve(ASSISTANT_ID)

def get_or_create_thread():
    if 'thread_id' not in st.session_state:
        thread = client.beta.threads.create(tool_resources={
  "file_search": {
    "vector_store_ids": ["VECTOR_STORE_ID"]
  }})
        st.session_state['thread_id'] = thread.id
    return st.session_state['thread_id']

def run_assistant_on_thread(thread_id):
   
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant.id
    )

    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        time.sleep(1)
    
  
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    
    for msg in messages.data:
        if msg.role == "assistant":
            return msg.content[0].text.value
    
    return "No initial response from assistant"


def get_assistant_response(prompt, thread_id):
    
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=prompt
    )
    
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant.id
    )
    
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        time.sleep(1)
    
    messages = client.beta.threads.messages.list(thread_id=thread_id)

    for msg in messages.data:
        if msg.role == "assistant":
            return msg.content[0].text.value
    
    return "No response from assistant"

def main():
    st.title("Agent Workflow Assistant")

    if 'messages' not in st.session_state:
        st.session_state.messages = []
        st.session_state.conversation_started = False

    thread_id = get_or_create_thread()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if not st.session_state.get('conversation_started', False):
  

        st.session_state.conversation_started = True
            

        with st.chat_message("assistant"):
            response = run_assistant_on_thread(thread_id)
            st.markdown(response)
            
    
        st.session_state.messages.append({
            "role": "assistant", 
            "content": response
            })
            

        st.rerun()

 
    if prompt := st.chat_input("Write your message here..."):

        st.session_state.messages.append({"role": "user", "content": prompt})
        

        with st.chat_message("user"):
            st.markdown(prompt)
        

        with st.chat_message("assistant"):
            response = get_assistant_response(prompt, thread_id)
            st.markdown(response)
        
 
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()