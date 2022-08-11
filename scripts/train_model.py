import os
import time
import toml
import gpt_2_simple as gpt


if __name__ == '__main__':
    # Training code here was adapted from https://github.com/minimaxir/gpt-2-simple
    model_name = '124M'
    config = toml.load('../config.toml')
    for folder in ['checkpoint/', 'samples/']:
        if os.path.isdir(folder):
            os.rmdir(folder)
    file_name = 'data/formatted/discord.txt'
    if not os.path.isdir(os.path.join('models', model_name)):
        print(f'Downloading base model {model_name} model...')
        gpt.download_gpt2(model_name=model_name)
    sess = gpt.start_tf_sess()
    print('Beginning to train... ', end='')
    start_time = time.time()
    gpt.finetune(sess, file_name, model_name=model_name, steps=config['Train-Step-Count'])
    end_time = time.time()
    print(f'model training finished, time taken: {end_time-start_time:.2f} seconds.')
