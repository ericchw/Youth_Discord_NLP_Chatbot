# https://huggingface.co/docs/transformers/installation
from transformers import pipeline

emotion = pipeline('sentiment-analysis', model='arpanghoshal/EmoRoBERTa')

emotion_labels = emotion("This is so stupid!")

print(emotion_labels)