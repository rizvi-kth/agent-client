import asyncio
import httpx
import json

async def main():
    url = "http://127.0.0.1:8081/test/me"
    
    # We use the 'stream' method to handle chunked responses.
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as response:
            
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
