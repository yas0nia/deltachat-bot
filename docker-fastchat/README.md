## Run FastChat with Deltachat

0. Install docker and docker-compose

1. configure email and pw in the compose.yml file

2. Run: `docker-compose up -d`

# Note if you have a nvidia gpu remove the --device cpu flag from the `python3 -m fastchat.serve.model_worker` Command in the FastChatDocker file
