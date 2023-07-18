import json

with open('training_prepared.jsonl', 'r', encoding="UTF-8") as json_file:
    json_list = list(json_file.readlines())
spacecount = 0
charCount = 0
previous = {}
tokenLengthAverage = 3
# counts spaces to estimate number of tokens
for i in range(len(json_list)):
    result = json.loads(json_list[i])
    currentPrompt = result["prompt"]
    currentCompletion = result["completion"]
    for c in range(len(currentPrompt)):
        if c % tokenLengthAverage == 0:
            charCount += 1
    for c in range(len(currentCompletion)):
        if c % tokenLengthAverage == 0:
            charCount += 1

def estimate(price):
    return (charCount/1000) * price

print(f"Ada: ${estimate(0.0004)}\nBabbage: ${estimate(0.0006)}\nCurie: ${estimate(0.003)}\nDavinci: ${estimate(0.03)}\nTurbo 3.5: {estimate(0.0015)}")