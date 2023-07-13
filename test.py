import openai
import random
import json

openai.api_key = "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"

filePath = "results.txt"

def RunTest(modelName, currentTest, preamble = ""):
    global prediction
    global response
    if(modelName == "gpt-3.5-turbo-0613"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"{preamble}{currentTest['prompt']} \"\"\""
                }
            ],
            temperature=1.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
        prediction = response["choices"][0]["message"]["content"]
    else:
        response = openai.Completion.create(
            model=modelName,
            prompt = currentTest["prompt"],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
        prediction = response["choices"][0]["text"]
    with open(filePath, 'a', encoding="UTF-8") as resultsFile:
        resultsFile.write(f"\nModel: {modelName} \nPrompt:{currentTest['prompt']}\nActual completion: {currentTest['completion']}Prediction: {prediction}\n")
        resultsFile.close()

trainedAda = "ada:ft-personal-2023-07-11-15-31-15"
trainedBabbage = "babbage:ft-personal-2023-07-13-12-23-04"
gptTurbo = "gpt-3.5-turbo-0613"
gptTurboPreamble = "Write a product line description for the following product name. The product description should be suitable to display the product on an online shopping website\n\nFor Example: \nProduct name: \"\"\"Awkward Styles Sugar Skull Shirts for Men Jolly Roger Skull and Crossbones Men's Tee Shirt Tops Day of Dead Tshirts Pirate Flag Shirts Skull T-shirts Dia de Los Muertos T Shirts for Men\"\"\"\n\nProduct Description: \"\"\"Are you planning a pirate themed party? Then this Awkward Styles Jolly Roger Skull &amp; Crossbones Graphic T-shirt Tops will be the perfect fit! This fun Jolly Roger Skull &amp; Crossbones Graphic T-shirt Tops wil also make a great gift for halloween, day of the dead, cinco de mayo, pirate lovers, birthdays and other special occasions or for everyday wear!| Aaaargh....Are you planning a pirate themed party? Then this Awkward Styles Jolly Roger Skull Graphic T-shirt Tops is the perfect fit! All Hands Hoay! Still searching for a Halloween costume? Why not go with this cool Jolly Roger Skull Graphic T-shirt Tops and be a pirate for the night. Perfect gift for Day of the Dead, Cinco de Mayo, Halloween, Birthdays or other special occasions! This Jolly Roger Skull Graphic T-shirt Tops is perfect for Halloween, Day of the Dead, Cinco de Mayo but it is also perfect for everyday wear! Celebrate the colorful mexican tradition in this cool Jolly Roger Skull Graphic T-shirt Tops 100% cotton Printed in the USA Available sizes: S-5XL Machine washable Available in a wide variety of sizes and colors\"\"\"\n##\nProduct Name: "

runNext = "Y"
while(runNext == "Y"):
    currentTest = {}
    with open('testing_prepared.jsonl', 'r', encoding="UTF-8") as json_file:
        json_list = list(json_file)
        currentTest = json.loads(json_list[random.randint(0, len(json_list) - 1)])
        json_file.close()
    print(currentTest["prompt"])
    RunTest(trainedAda, currentTest)
    RunTest(trainedBabbage, currentTest)
    RunTest(gptTurbo, currentTest, gptTurboPreamble)
    runNext = input("Run the program again?")
    