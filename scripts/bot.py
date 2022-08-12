import toml
import aiohttp
import gpt_2_simple as gpt2
from discord.ext.commands import *
from discord import Webhook, AsyncWebhookAdapter


class DialogueGen(Cog):

    def __init__(self, bot, webhook_url):
        self.bot = bot
        self.webhook_url = webhook_url
        self.user_cache = {}
        self.sess = gpt2.start_tf_sess()
        print('Loading model... ')
        gpt2.load_gpt2(self.sess)
        print('Finished loading model!')

    @Cog.listener()
    async def on_ready(self):
        print('Bot is now ready!')

    @Cog.listener()
    async def on_command_error(self, error):
        if isinstance(error, CommandNotFound):
            return

    @is_owner()
    @command(aliases=['generate'])
    async def generate_command(self, ctx, temp: float, length: int):
        await ctx.send('Generating...')
        async with ctx.typing():
            script = gpt2.generate(self.sess, return_as_list=True, length=length, temperature=temp)[0]
            await ctx.send('-------------------------- Begin Response --------------------------')
            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url(self.webhook_url, adapter=AsyncWebhookAdapter(session))
                for line in script.split('\n'):
                    # Not quite sure what's causing this issue but if I had to guess
                    # GPT2 is generating lines that don't begin with `<id>:` which
                    # breaks the string splitting which is why this entire try block exists
                    try:
                        line_data = line.split(':', 1)
                        user_id, bot_text = int(line_data[0]), line_data[1][:2000]
                        if bot_text:
                            if user_id not in self.user_cache:
                                user = await self.bot.fetch_user(user_id)
                                user_avatar_url = user.avatar_url
                                user_name = user.name
                                self.user_cache[user_id] = (user_name, user_avatar_url)
                            name, avatar_url = self.user_cache[user_id]
                            await webhook.send(content=bot_text, username=name, avatar_url=avatar_url)
                    except Exception as e:
                        print(f'Exception occurred: {e}')
            await ctx.send('-------------------------- End Response --------------------------')


if __name__ == '__main__':
    config = toml.load('../config.toml')
    bot = Bot(command_prefix='!')
    bot.add_cog(DialogueGen(bot, config['Webhook-URL']))
    bot.run(config['Bot-Token'])
