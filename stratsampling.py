import pandas as pd
import json
import random
# stratisfied sampling for sourcing data to train/test the open ai models
# orgranise the csv into a dictionary of dictionaries
 
strata = {"0" : []}
strataDensity = 25
testFile = pd.read_csv("walmart_com-ecommerce_product_details.csv")
for i in range(len(testFile)):
    current = testFile.loc[i]
    if(str(current["Sale Price"]) == "nan"): 
        continue
    key = str(round(current["Sale Price"] / strataDensity))
    try: 
        strata[key].append({
            "prompt" : current["Product Name"],
            "completion": current["Description"]
        })
    except:
        strata.update({key: []})
        strata[key].append({
            "prompt" : current["Product Name"],
            "completion": current["Description"]
        })

# randomly sample some values from each strata and put them in either training or testing
def writeJson(sample, filepath):
    json_lines = [json.dumps(l) for l in sample]
    json_data = '\n'.join(json_lines)
    with open(filepath, 'a') as f:
        f.write("\n"+json_data)

training = open("training.jsonl",  "r+")
training.truncate(0)
training.close()

testing = open("testing.jsonl", "r+")
testing.truncate(0)
testing.close()

# randomly selects items from each strata
for stratum in strata:
    try:
        sample = random.sample(strata[stratum], k = 2)
        writeJson(sample, "testing.jsonl") #testing
    except(ValueError):
        writeJson(strata[stratum], "testing.jsonl")
    try:
        sample = random.sample(strata[stratum], k = 100)
        writeJson(strata[stratum], "training.jsonl") #training
    except(ValueError):
        writeJson(strata[stratum], "training.jsonl")