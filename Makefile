
server:
	uv run uvicorn main:app --port 8081 --reload


client:
	uv run python chat_cli.py


sclient:
	uv run streamlit run client_slt.py
