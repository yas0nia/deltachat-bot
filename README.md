# A repository for a Digital Resistance Lab Hackathon problem "Self-hosted LLM with an interface to the messenger Delta Chat", Berlin April 2023

## Installation

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

### 3. Setup a delta-rpc-server for a Delta Chat bot and a delta-rpc-client, don’t forget to add delta-rpc-server to your path!

### 4. Run the bot! 
