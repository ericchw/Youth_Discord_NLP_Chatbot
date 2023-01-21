# https://huggingface.co/docs/transformers/installation
from transformers import pipeline
# from google_trans_new import google_translator  
from googletrans import Translator
# pip uninstall googletrans==4.0.0-rc1
# pip install googletrans==3.1.0a0
# must uninstall first then install
from googletrans import LANGUAGES

emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')

def emtransform(text):
    # translat = google_translator()
    translat = Translator()
    # for lang in LANGUAGES:
    #     print(f'{lang} - {LANGUAGES[lang]}')
    trans = translat.translate('text')
    # trans = translat.translate('他真的是白痴',lang_src='zh-tw', lang_tgt='en')
    # print(trans.text)
    emotion_labels = emotion(trans.text)

    print(emotion_labels)
    return emotion_labels