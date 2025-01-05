from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
import json

app = FastAPI()

@app.get("/test/me")
async def test_me():
    """Return three JSON objects in a streaming fashion, each after a 3-second delay."""
    
    async def generator():
        # First object
        data_one = {"item": "chunk_1", "country": "Sweden"}
        data_two = {"item": "chunk_2", "country": "USA"}
        data_three = {"item": "chunk_3", "country": "Bangladesh"}
        data_arr = [data_one, data_two, data_three]
        
        for _data in data_arr:
            await asyncio.sleep(3)
            yield json.dumps(_data) + "<buffer_break>"
            
            
        # return json.dumps(data_one) + "\n"
        # await asyncio.sleep(3)

        # # Second object
        # return json.dumps(data_two) + "\n"
        # await asyncio.sleep(3)

        # # Third object
        # yield json.dumps(data_three) + "\n"

    # We use StreamingResponse so that each JSON is streamed separately
    return StreamingResponse(generator(), media_type="application/json")
