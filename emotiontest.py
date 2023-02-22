# https://huggingface.co/docs/transformers/installation
from transformers import pipeline
# from google_trans_new import google_translator  
from googletrans import Translator
# pip uninstall googletrans==4.0.0-rc1
# pip install googletrans==3.1.0a0
# must uninstall first then install
from googletrans import LANGUAGES

# emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

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
            return_label = item['label']

    # print(emotion_labels)
    return return_label
