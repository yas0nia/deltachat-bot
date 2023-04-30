import asyncio
import json
from llama_cpp import Llama

async def fetch_llm_reply(message):
    response = await get_alpaca_response(message)
    return response

async def get_alpaca_response(message):
    llm = Llama(model_path="ggml-alpaca-7b-q4.bin")
    output = llm(f"Q: {message} A: ", max_tokens=100, stop=["Q:", "\n"], echo=True)
    message = output['choices'][0]['text']
    #strip the Q: and A: from the message string, take only things after A: 
    response = message.split("A: ")[1]
    return response