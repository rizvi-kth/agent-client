# Sample client for Agents

## Install UV

Install UV from : https://docs.astral.sh/uv/getting-started/installation/

#### Prepare the UV environment
- `uv init`
- `uv add fastapi uvicorn streamlit`
 

#### Run the sample Server
 
 - ``uv run uvicorn main:app --port 8081 --reload``


 #### Run the sample Client 
- `uv run python chat_cli.py`

 #### Run the Streamlit Client 
  - ``uv run streamlit run client_slt.py``



 Use non-buffer mode to test the streaming
 - curl --no-buffer http://127.0.0.1:8081/test/me
 
 
 
curl --no-buffer -X POST http://127.0.0.1:8008/ask/v3/achat \
-H "Content-Type: application/json" \
-d '{
  "user_id": "u1",
  "email": "string",
  "is_first_question": true,
  "chat_memory": [],
  "company": "",
  "start_date": "2025-01-01",
  "end_date": "2025-01-03",
  "my_query": "Hi, My name is Rizvi!"
}'



