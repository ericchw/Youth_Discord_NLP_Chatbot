# https://huggingface.co/docs/transformers/installation
from transformers import pipeline
# from google_trans_new import google_translator  
from googletrans import Translator
# pip uninstall googletrans==4.0.0-rc1
# pip install googletrans==3.1.0a0
# must uninstall first then install
from googletrans import LANGUAGES
import os

#Avoid download model again if restart Docker
MODEL_DIR = '/python_app/model'
MODEL_PATH = os.path.join(MODEL_DIR, 'emotion-english-distilroberta-base')
if os.path.exists(MODEL_PATH):
    # Load the model from the mounted volume
    classifier = pipeline("text-classification", model=MODEL_PATH, top_k=None)
else:
    # Download the model and save it to the mounted volume
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)
    classifier.save_pretrained(MODEL_PATH)
# # emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')
# classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

# from transformers import pipeline
# classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)


def emtransform(text):
    # translat = google_translator()
    translat = Translator()
    # for lang in LANGUAGES:
    #     print(f'{lang} - {LANGUAGES[lang]}')
    trans = translat.translate(text)
    # trans = translat.translate('他真的是白痴',lang_src='zh-tw', lang_tgt='en')
    emotion_labels = classifier(trans.text)
    max_score = 0
    return_label =''
    for item in emotion_labels[0]:
        if item['score'] > max_score:
            max_score = item['score']
            return_label = item

    # print(emotion_labels)
    return return_label
