import json

with open('training.jsonl', 'r') as json_file:
    json_list = list(json_file)

spacecount = 0
previous = {}
for i in range(len(json_list)):
    result = json.loads(json_list[i])
    currentPrompt = result["prompt"]
    currentCompletion = result["completion"]
    if(currentPrompt == previous): # disregarding duplicates
        continue
    # count the spaces 
    for c in str(currentPrompt):
        if c == ' ':
            spacecount += 1
    for c in str(currentCompletion):
        if c == ' ':
            spacecount += 1
    previous = currentPrompt

print(spacecount)
def estimate(price):
    return spacecount * price/1000

print(f"Ada: ${estimate(0.0004)} \n Babbage: ${estimate(0.0006)} \n Curie: ${estimate(0.003)} \n Davinci: ${estimate(0.03)}" )