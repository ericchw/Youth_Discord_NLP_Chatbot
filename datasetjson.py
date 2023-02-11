import json

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
with open('intents.json', 'r') as json_file:
    # json.dump(data, json_file)
     data = json.load(json_file)
    #  for i in data['intents']:
    #      print(i)

with open('summer_wild_evaluation_dialogs.json', 'r') as json_file:
    # json.dump(data, json_file)
     summer = json.load(json_file)
print(summer)    
new_intent = ""

temp_intent = {
        "tag": "",
        "patterns": [
            
        ],
        "responses": [
            
                
            
        ]
    }
human = ""
bot = "" 
h_ent = 0
b_ent = 0
for i in summer:
    temp = i
    temp_intent['tag'] = temp['dialog_id']
    # print(temp)
    for x in enumerate(temp['dialog']):
        print(x[1])
        if 'participant1' in x[1].values():
            # print(f"human: {x[1]['text']}")
            human = x[1]['text']
            h_ent = h_ent + 1
            temp_intent['responses'].append(human)
        else:
            bot = x[1]['text']
            b_ent = b_ent + 1
            temp_intent['patterns'].append(bot)
            # print(f"bot: {x[1]['text']}")

        if b_ent==1 and h_ent == 1:
            data['intents'].append(temp_intent)
            b_ent = 0
            h_ent = 0
            temp_intent = {
            "tag": temp['dialog_id'],
            "patterns": [
            ],
            "responses": [
            ]
        }
        # print(new_intent)
        # data['intents'].append(temp_intent)
        # print(data)

        # print(data)
        # new_data = json.dumps(data, indent=4)

        with open("intents.json", "w") as file:
            # Write the modified data back to the file
            json.dump(data, file)
            # file.write(new_data)
        
    break
            
        # for p,y in x[1].items():
        #     if 'Human' in x[1].values():
        #         print(p, y)
    # print(new_intent)  
