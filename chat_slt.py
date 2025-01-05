import streamlit as st
import asyncio
import httpx
import json

# Httpx section
async def post(msg, id):
    payload = {
        "user_id": id,
        "email": "string",
        "is_first_question": True,
        "chat_memory": [],
        "company": "",
        "start_date": "2025-01-01",
        "end_date": "2025-01-03",
        "my_query": msg
    }
    url = "http://0.0.0.0:8008/ask/v3/achat"
    
    # We use the 'stream' method to handle chunked responses.
    async with httpx.AsyncClient(timeout = httpx.Timeout(connect=5.0, read=10.0, write=5.0, pool=30.0)) as client:
        async with client.stream("POST", url, json=payload) as response:
            
            # We’ll maintain a buffer in case chunks don’t align with newline boundaries.
            buffer = ""
            
            # aiter_text() yiel
            # ds text as it's received from the server.
            async for chunk in response.aiter_text():
                buffer += chunk
                
                # Split on newline to separate individual JSON objects
                while "<buffer_break>" in buffer:
                    line, buffer = buffer.split("<buffer_break>", 1)
                    
                    # Safeguard to ignore empty lines (if any)
                    line = line.strip()
                    if not line:
                        continue
                    
                    # Parse and display each JSON dictionary
                    data = json.loads(line)
                    yield data



# Streamlit section
with st.sidebar:
    st.title("💬 Playground")
    st.caption("🚀 Text-Text Models")
    
    
if "messages" not in st.session_state:
    st.session_state["messages"] = [] 


# async def handle_user_input():
#     user_message = st.session_state["user_input"]  # Retrieve the input from session state
#     st.session_state.messages.append({"role": "user", "content": user_message})    
#     response_content = await post(user_message, "usr_1")
#     st.session_state.messages.append({"role": "ai", "content": response_content})

# Display chat input with callback
# st.chat_input("Type your message here...", key="user_input", on_submit=handle_user_input)

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])
#     print(msg)

user_message = st.chat_input("Type your message here...", key="user_input")

# Update Chat-Component from the Session-Component
if user_message:
    st.chat_message("user").write(user_message)
    st.chat_message("ai").write_stream(post(user_message, "usr_1"))
