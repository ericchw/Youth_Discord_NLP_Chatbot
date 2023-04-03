import random
import jieba

# load dataset
import json
with open('data.json', 'r',encoding='utf-8') as f:
    intents = json.load(f)

# create a dictionary to store all patterns
patterns = {}
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # use jieba to tokenize the pattern
        tokens = jieba.lcut(pattern)
        for token in tokens:
            # only consider tokens that are not stopwords
            if token not in [' ', '\n'] and token not in patterns:
                patterns[token] = [intent['tag']]
            elif token in patterns:
                patterns[token].append(intent['tag'])

# define a function to get the response
def get_response(input_text):
    # tokenize the input text
    tokens = jieba.lcut(input_text)
    # find matching patterns
    matching_patterns = []
    for token in tokens:
        if token in patterns:
            matching_patterns.extend(patterns[token])
    # select a random response from the matching patterns
    if matching_patterns:
        tag = random.choice(matching_patterns)
        for intent in intents['intents']:
            if intent['tag'] == tag:
                response = random.choice(intent['responses'])
                return response
    else:
        return "Sorry, I do not understand"

