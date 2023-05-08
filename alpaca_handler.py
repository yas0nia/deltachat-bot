import config
import asyncio
import json
from llama_cpp import Llama

def fetch_llm_reply(message):
    response = get_alpaca_response(message)
    return response

def get_alpaca_response(message):
    assistant_prompt = "BOT: "
    llm = Llama(model_path=config.modelpath)
    #output = llm(f"Q: {message} A: ", max_tokens=200, stop=["Q:", "\n"], echo=True)
    #llm = Llama(model_path="ggml-vic7b-q5_0.bin")
    prompt = f"HUMAN: {message}\n\n  BOT:"
    prompt_len = len(llm.tokenize(b" " + prompt.encode("utf-8")))
    print("Prompt len: ", prompt_len)
    max_tokens = 128
    if prompt_len >= max_tokens:
        return "TLDR"
    output = llm(prompt, max_tokens=max_tokens - prompt_len, stop=["HUMAN:"], echo=True)

    print(output)
    message = output['choices'][0]['text']
    #strip the Q: and A: from the message string, take only things after A: 
    #response = message.split("A: ")[1]
    print(message)
    response = message.split(assistant_prompt)[1]
    return response
