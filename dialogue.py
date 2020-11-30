import json
import random

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
    input_text = input()

    sample_category = random.choices(list(configuration.keys()), weights = list(configuration.values()))[0]
    sample_prompt = random.choice(prompts[sample_category])

    print('\n' + sample_prompt)
