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

import langid

def is_english(text):
    lang, _ = langid.classify(text)
    return lang == 'en'

text = "This is an example sentence in English."
if is_english(text):
    print("The text is in English.")
else:
    print("The text is not in English.")


