import random
import time

foods = {}

def get_random_lunch():
    with open('./lunch.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for i in range(0, len(lines), 2):
            key = lines[i+1].strip()
            value = lines[i].strip()
            foods[key] = value

    seed = int(time.time())
    random.seed(seed)

    random_key = random.choice(list(foods.keys()))
    random_value = foods[key]

    return random_key, random_value
