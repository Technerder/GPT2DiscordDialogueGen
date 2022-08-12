import os
import time
import toml
import shutil
import gpt_2_simple as gpt


if __name__ == '__main__':
    # Training code here was adapted from https://github.com/minimaxir/gpt-2-simple
    config = toml.load('../config.toml')
    model_name = config['Base-Model-Name']
    file_name = 'data/formatted/discord.txt'
    for folder in ['checkpoint/', 'samples/']:
        shutil.rmtree(folder, ignore_errors=True)
    if not os.path.isdir(os.path.join('models', model_name)):
        print(f'Downloading base model {model_name} model.')
        gpt.download_gpt2(model_name=model_name)
        print('Base model download complete.')
    sess = gpt.start_tf_sess()
    print('Beginning to train...')
    start_time = time.time()
    gpt.finetune(sess, file_name, model_name=model_name, steps=config['Train-Step-Count'])
    end_time = time.time()
    print(f'Model training finished, time taken: {end_time-start_time:.2f} seconds.')
