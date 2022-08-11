# GPT2DiscordDialogueGen
The code is terrible but the bot makes people laugh so its gotta be decent

# Prerequisites
- [Anaconda](https://www.anaconda.com/) - Installing the annoying to install libraries (`CUDA`, `cuDNN`, `Tensorflow`)
- [git](https://git-scm.com/) - Cloning the repo

# Setup
1. `conda create test-env`
2. `conda activate test-env`
3. `conda install pytorch cudatoolkit=11.3.1 cudnn=8.2.1`
4. `git clone https://github.com/Technerder/GPT2DiscordDialogueGen`
5. `cd GPT2DiscordDialogueGen`
6. `pip install -r requirements.txt`
7. Populate all fields in the `config.toml` file

# Running
For the Discord bot to work you'll need to go through the following steps in order

### Scrape Messages
This script will spin up the Discord bot and scrape all messages from all users in the `Consenting-Users` in all but the `Ignored-Channels` channels.
- `python scrape_data.py`

### Format Messages
This script will format all messages in the files within the `scripts/data/raw` and combine them into a single file to train the model off
- `python format_data.py`

### Train model on messages
This script will train the model on all messages the bot managed to scrape. This script can take up to/over 30 minutes from my experience (RTX 3060 12GB)
- `python train_model.py`

### Run the bot
- `python bot.py`

# Common Issues / Notes
- On Linux/Mac you might need to substitute `python` with `python3` and `pip` with `pip3` for some commands
- If the bot fails to scrape messages, it might be because it lacks permission to view the content of Discord messages, in which case you'll need to manually enable the `message content` intent in the [Discord Developers Portal](https://discord.com/developers/applications) under `YourBot>Bot>Message Content Intent`

# Todo
- Dockerize the entire repository (probably with [nvidia-docker](https://github.com/NVIDIA/nvidia-docker))