import re
import glob
import cleantext


if __name__ == '__main__':
    for filepath in glob.iglob('data/raw/*.txt'):
        with open('data/formatted/discord.txt', 'a', encoding='UTF8') as output:
            with open(filepath, encoding='UTF8') as mini_file:
                for line in mini_file.readlines():
                    # https://www.reddit.com/r/Discord_Bots/comments/iicffv/if_anyone_needs_regex_to_match_an_emote_mention/
                    line = re.sub("<(?::\w+:|@!*&*|#)[0-9]+>", '', line)
                    line = cleantext.clean(line, fix_unicode=True, lower=False, no_emoji=True, no_urls=True, replace_with_url='')
                    output.write(f'{line}\n')
