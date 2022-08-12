# GPT2DiscordDialogueGen
This repository allows you to train a machine learning model (specifically `gpt2`) to generate a semi-accurate (really stretching the definition here) dialogue similar to the ones taking place in the Discord server it was trained off of. The code is terrible but the bot makes people laugh so its gotta be decent.

# Prerequisites
- [Anaconda](https://www.anaconda.com/) - Installing the annoying to install libraries (`CUDA`, `cuDNN`, `Tensorflow`)
- [git](https://git-scm.com/) - Cloning the repo

# Setup
```bash
# Create conda environment
conda create --name test-env
# Activate conda environment
conda activate test-env
# Install required dependencies
conda install cudatoolkit=11.3.1 cudnn=8.2.1
# Clone repo
git clone https://github.com/Technerder/GPT2DiscordDialogueGen
# Go into the repo directory
cd GPT2DiscordDialogueGen
# Install required python dependencies
pip3 install -r requirements.txt
# Go into the scripts directory 
cd scripts
```

# Run
Before you can run the bot you'll want to edit the `config.toml` file to include everything the bot needs to run.
```bash
# This script will spin up the Discord bot and scrape all messages from all 
# users in the `Consenting-Users` in all but the `Ignored-Channels` channels.
python3 scrape_data.py

# This script will spin up the Discord bot and scrape all messages from all 
# users in the `Consenting-Users` in all but the `Ignored-Channels` channels.
python3 scrape_data.py

# This script will format all messages in the files within the `scripts/data/raw` 
# and combine them into a single file to train the model off
python3 format_data.py

# This script will train the model on all messages the bot managed to scrape. 
# This script can take up to/over 30 minutes from my experience (RTX 3060 12GB)
python3 train_model.py

# This script will start the Discord bot
python3 bot.py
```

### Generating Dialogue
To generate dialogue go into any text channel the bot has access to and type `!generate <temp> <length>` where:
- `temp` is a decimal number between 0.0 and 1.0 (0.7 seems to produce the best results)
- `length` is the length of the dialogue

# Common Issues / Notes
- If the bot fails to scrape messages, it might be because it lacks permission to view the content of Discord messages, in which case you'll need to manually enable the `message content` intent in the [Discord Developers Portal](https://discord.com/developers/applications) under `YourBot>Bot>Message Content Intent`

# Todo
- Dockerize the entire repository (probably with [nvidia-docker](https://github.com/NVIDIA/nvidia-docker))
- Swap over project to use the newer [aitextgen](https://github.com/minimaxir/aitextgen)
- Use a proper logging library instead of just using `print`