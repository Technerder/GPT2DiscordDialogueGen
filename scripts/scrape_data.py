import os
import toml
import glob
from discord.ext.commands import Bot


bot = Bot(command_prefix='!')
config = toml.load('../config.toml')


@bot.event
async def on_ready():
    guild_id = config['Guild-ID']
    ignored_channels = config['Ignored-Channels']
    consenting_users = config['Consenting-Users']
    guild = bot.get_guild(guild_id)
    raw_data_path = 'data/raw'
    for file in glob.glob(f'{raw_data_path}/*.txt'):
        os.remove(file)
    for text_channel in guild.text_channels:
        if text_channel.id not in ignored_channels:
            print(f'Scraping #{text_channel}')
            with open(f'{raw_data_path}/{text_channel.id}.txt', 'a', encoding='utf-8') as output_file:
                for message in await text_channel.history(limit=None).flatten():
                    author_id = message.author.id
                    if author_id in consenting_users:
                        text = message.content.replace('\n', ' ').strip()
                        if not text.isspace():
                            output_file.write(f'{author_id}:{text}\n')
    await bot.close()


if __name__ == '__main__':
    os.makedirs('data/raw/', exist_ok=True)
    bot.run(config['Bot-Token'])
