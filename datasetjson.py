import json, nltk, uuid

# data = {}
# data['intents'] = []

# with open('dialogs.txt', 'r') as file:
#     for line in file:
#         text = line.strip().split('\t')
#         tag = text[0]
#         patterns = [text[1]]
#         responses = [{"text": text[2]}]
#         data['intents'].append({
#             "tag": tag,
#             "patterns": patterns,
#             "responses": responses
#         })
with open('intents.json', 'r', encoding='utf-8') as json_file:
    # json.dump(data, json_file)
     data = json.load(json_file)
    #  for i in data['intents']:
    #      print(i)



# text = "Guru99 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
# lower_case = text.lower()
# tokens = nltk.word_tokenize(lower_case)
# tags = nltk.pos_tag(tokens)
# for tag in tags:
#     if 'NN' in tag:
#         print(tag[0])
#     break
# counts = Counter( tag for word,  tag in tags)
# print(counts)

temp_intent = {
        "tag": "",
        "patterns": [
            
        ],
        "responses": [
            
                
            
        ]
    }

with open('WikiQA-dev.txt', 'r') as f:

    counter = 1
    current = ""
    for line in f:
        # Extract the first sentence before the tab space
        pattern = line.split('\t')[0].strip('.!?')
        response = line.split('\t')[1].strip('.!?')
        if current != pattern:
            data['intents'].append(temp_intent)
            temp_intent = {
                "tag": '',
                "patterns": [
                ],
                "responses": [
                ]
            }
            temp_intent['tag'] = str(counter)
            counter += 1
            current = pattern
            lower_case = pattern.lower()
            tokens = nltk.word_tokenize(lower_case)
            tags = nltk.pos_tag(tokens)
            for tag in tags:
                if 'VBP' or 'NN' or 'NNS' or 'NNP' in tag:
                    temp_intent['patterns'].append(tag[0])
                print(tag)
                    # break
            temp_intent['responses'].append(response)
        else:
            temp_intent['responses'].append(response)
        
        
        
        
        # temp_intent['patterns'].append(pattern)
        
        
        
        with open("intents.json", "w",encoding='utf-8') as file:
            # Write the modified data back to the file
            json.dump(data, file, ensure_ascii=False, indent=4)
            # file.write(new_data)
        # if counter == 3:
        #     print(data['intents'])
        #     break