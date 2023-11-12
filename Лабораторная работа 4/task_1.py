# TODO решите задачу

import json

filename = 'input.json'
result = 0.0

def task() -> float:
    global result
    with open(filename) as file:
        data = json.load(file)
    for i in data:
        if i["weight"] and i["score"] is not None:
            result = result + (i["weight"] * i["score"])
    return result
print(f"{task():.3f}")
