import os
import openai
import random
import json

openai.api_key = "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"
runNext = "Y"

filePath = "results.txt"
while(runNext == "Y"):
    currentTest = {}
    with open('testing_prepared.jsonl', 'r', encoding="UTF-8") as json_file:
        json_list = list(json_file)
        currentTest = json.loads(json_list[random.randint(0, len(json_list) - 1)])
        json_file.close()
    response = openai.Completion.create(
        model="ada:ft-personal-2023-07-11-15-31-15",
        prompt=currentTest["prompt"],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    with open(filePath, 'a', encoding="UTF-8") as resultsFile:
        resultsFile.write(f"Prompt:{currentTest['prompt']}\nActual completion: {currentTest['completion']}Prediction: {response['choices'][0]['text']}\n")
        resultsFile.close()
    runNext = input("Run the program again?")
    if(runNext != "Y"):
        break

"""adafile = open("adaresults.txt", "a",encoding="UTF-8")
resultsFile = open(filePath, "r", encoding="UTF-8")
for line in (resultsFile.readlines()):
    print(line)
    adafile.write(line)
resultsFile.close()
adafile.close()"""