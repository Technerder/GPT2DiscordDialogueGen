import re
import os
import glob
import cleantext


if __name__ == '__main__':
    os.makedirs('data/formatted/', exist_ok=True)
    output_file_name = 'data/formatted/discord.txt'
    if os.path.exists(output_file_name):
        os.remove(output_file_name)
    print('Beginning to format data.')
    for filepath in glob.iglob('data/raw/*.txt'):
        with open(output_file_name, 'a', encoding='UTF8') as output:
            with open(filepath, encoding='UTF8') as mini_file:
                for line in mini_file.readlines():
                    # https://www.reddit.com/r/Discord_Bots/comments/iicffv/if_anyone_needs_regex_to_match_an_emote_mention/
                    line = re.sub("<(?::\w+:|@!*&*|#)[0-9]+>", '', line)
                    line = cleantext.clean(line, fix_unicode=True, lower=False, no_emoji=True, no_urls=True, replace_with_url='')
                    # Only save lines with text
                    if line.split(':', 1)[1].strip():
                        output.write(f'{line}\n')
    print('Formatting complete!')
