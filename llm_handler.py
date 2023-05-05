import aiohttp
import json


async def fetch_llm_reply(message):
    # extend to other llms
    response = await get_fastchat_response(message)
    return response


async def get_fastchat_response(message):
    url = "http://fastchat:8000/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "fastchat-t5-3b-v1.0",
        "messages": [{"role": "user", "content": f"{message}"}],
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url, headers=headers, data=json.dumps(data)
        ) as response:
            result = await response.text()
    result_dict = json.loads(result)
    message = result_dict["choices"][0]["message"]["content"]
    print(message)
    return str(message)
