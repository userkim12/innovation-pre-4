import random
import time
from pymongo import MongoClient
client = MongoClient('mongodb+srv://KSH:1111@cluster0.yrsyosy.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


def get_random_message():     
    seed = int(time.time())
    random.seed(seed)

    random_id = random.choice(range(1,15))
    random_data = db.advices.find_one({'id':random_id}, {'_id':False})
    random_author = random_data['author']
    random_comment = random_data['comment']

    return random_author, random_comment


def get_random_lunch():
    seed = int(time.time())
    random.seed(seed)

    random_id = random.choice(range(1,15))
    random_data = db.lunchs.find_one({'id':random_id}, {'_id':False})
    random_foodname = random_data['foodname']
    random_img = random_data['img']
    
    return random_foodname, random_img


# show_random_message()
# get_random_lunch()