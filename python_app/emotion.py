from googletrans import Translator
from nrclex import NRCLex


def nrcdectect(text):
    emotion = NRCLex(text)
    feel=emotion.top_emotions
    return feel


def transform(text):
    #translation=ts.google(text, from_language='zh-TW', to_language='en')
    translator = Translator()
    translation = translator.translate(text, dest='en')
    print(translation.text)
    return nrcdectect(translation.text)

print(nrcdectect('i\'m not happy'))