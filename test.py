import os
import openai
import random

openai.api_key = "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"
runNext = "Y"
while(runNext == "Y"):
    response = openai.Completion.create(
        model="text-ada-001",
        prompt="Write a headline for an article about pythagoras",
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    with open('training_prepared.jsonl', 'r', encoding="UTF-8") as json_file:
        json_list = list(json_file)
        currentTest = json_list[random.randint(0, len(json_list) - 1)]
        json_file.close()
    with open('results.txt', 'a', encoding="UTF 8") as resultsFile:
        resultsFile.write(f"Actual completion: {currentTest['completion']}, Prediction: {response}")
    runNext = input("Run the program again?")
