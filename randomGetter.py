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


def get_random_luck():
    seed = int(time.time())
    random.seed(seed)

    random_id = random.sample(range(1,100),3)

    random_data1 = db.lucks.find_one({'id':random_id[0]}, {'_id':False})
    random_data2 = db.lucks.find_one({'id':random_id[1]}, {'_id':False})
    random_data3 = db.lucks.find_one({'id':random_id[2]}, {'_id':False})

    random_card1 = random_data1['luck']
    random_card2 = random_data2['luck']
    random_card3 = random_data3['luck']

    return random_card1,random_card2,random_card3


# show_random_message()
# get_random_lunch()