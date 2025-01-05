import asyncio
import httpx
import json

payload = {
        "user_id": "uid_2",
        "email": "string",
        "is_first_question": True,
        "chat_memory": [],
        "company": "",
        "start_date": "2025-01-01",
        "end_date": "2025-01-05",
        "my_query": "What is the latest news about Apple?"
    }

async def main():
    url = "http://127.0.0.1:8008/ask/v3/achat"
    
    # We use the 'stream' method to handle chunked responses.
    async with httpx.AsyncClient() as client:
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
                    print("Received:", data)

if __name__ == "__main__":
    asyncio.run(main())
