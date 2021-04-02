import os
import json
import random
import sys

prompts = json.load(open('prompts.json'))

configuration = {
    "Remember": 10,
    "Understand": 10,
    "Apply": 10,
    "Analyze": 10,
    "Evaluate": 10,
    "Create": 10
}

while True:
    answer = input()

    sample_category = random.choices(list(configuration.keys()), weights = list(configuration.values()))[0]
    sample_prompt = random.choice(prompts[sample_category])

    print('\n' + sample_prompt)
    
    res = open(os.path.join(sys.path[0], "Export.txt"), "a")
    res.write(sample_prompt + "\n" + answer + "\n\n\n")
    res.close()
