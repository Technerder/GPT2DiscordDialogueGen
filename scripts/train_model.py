import os
import gpt_2_simple as gpt


if __name__ == '__main__':
    train = True
    model_name = '124M'
    file_name = 'data/formatted/discord.txt'
    if not os.path.isdir(os.path.join('models', model_name)):
        print(f'Downloading {model_name} model...')
        gpt.download_gpt2(model_name=model_name)
    sess = gpt.start_tf_sess()
    if train:
        gpt.finetune(sess, file_name, model_name=model_name, steps=10000, save_every=1000)
    else:
        gpt.load_gpt2(sess)
    print(gpt.generate(sess))
