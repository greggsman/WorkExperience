import json

with open('training_prepared.jsonl', 'r', encoding="UTF-8") as json_file:
    json_list = list(json_file.readlines())

spacecount = 0
previous = {}
# counts spaces to estimate number of tokens
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