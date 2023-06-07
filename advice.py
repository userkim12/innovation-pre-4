import random
import time

f = open("./advice.txt", 'r')

def show_random_message(): 
    messages = {}
    with open('./advice.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for i in range(0, len(lines), 2):
            key = lines[i+1].strip()
            value = lines[i].strip()
            messages[key] = value

    seed = int(time.time())
    random.seed(seed)

    random_key = random.choice(list(messages.keys()))
    random_value = messages[random_key]

    return random_key, random_value

show_random_message()