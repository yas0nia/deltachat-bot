# A repository for a Digital Resistance Lab Hackathon problem "Self-hosted LLM with an interface to the messenger Delta Chat", Berlin April 2023

## This README contains two installation guides: Easy installation with Alpaca LLM for low resources environment (you have a laptop with 8GB RAM and you're not deep into LLMs) or an experimental FastChat installation (will be really slow for noGPU environments)


## Easypeasy installation with ```alpaca.cpp```

0. Install requirements: ``` pip install -r requirements.txt ```

1. Download the model from here: https://huggingface.co/Sosaka/Alpaca-native-4bit-ggml/blob/main/ggml-alpaca-7b-q4.bin

2. Download deltachat-rpc-server and make sure its in your PATH https://github.com/deltachat/deltachat-core-rust/tree/master/deltachat-rpc-server

3. Install deltachat-rpc-client for Python https://github.com/deltachat/deltachat-core-rust/tree/master/deltachat-rpc-client

4. Put the model step 1. to the folder with the echobot.py

5. Start your bot by running ```python echobot.py BOT_MAIL BOT_PASSWD```


## FastChat implementation 

### 1. Prepare an LLM (Vicuna 7B, 13B or Fast Chat): https://github.com/lm-sys/FastChat

Here’s how we did in on with MacOS (Apple Silicon, M1) - CPU only mode:

```
pip3 install fschat #or install  from source

#install git-lfs and clone a required model from huggingface:

brew install git-lfs
git lfs install
git clone https://huggingface.co/lmsys/fastchat-t5-3b-v1.0
```

### 2. Set up an OpenAI-like RESTful API (Again, link to the source documentation: https://github.com/lm-sys/FastChat)

```
python3 -m fastchat.serve.controller
python3 -m fastchat.serve.model_worker --model-name 'fastchat-t5-3b-v1.0' --model-path lmsys/fastchat-t5-3b-v1.0 --device cpu
export FASTCHAT_CONTROLLER_URL=http://localhost:21001
python3 -m fastchat.serve.api --host localhost --port 8000

#test it
 curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "fastchat-t5-3b-v1.0",
    "messages": [{"role": "user" "content": "Hello!"}]
  }'
```

### 3. Setup a delta-rpc-server for a Delta Chat bot and a delta-rpc-client

  First, download the deltachat-rpc-server and make sure its in your PATH https://github.com/deltachat/deltachat-core-rust/tree/master/deltachat-rpc-server

  Then, install deltachat-rpc-client for Python https://github.com/deltachat/deltachat-core-rust/tree/master/deltachat-rpc-client

### 4. Run the bot: ```python echobot.py BOT_MAIL BOT_PASSWD```
