from pymongo import MongoClient
client = MongoClient('mongodb+srv://KSH:1111@cluster0.yrsyosy.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

f = open("./advice.txt", 'r')

def set_advice_data(): 
    messages = {}
    with open('./advice.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        id=1
        for i in range(0, len(lines), 2):
            author = lines[i+1].strip()
            comment = lines[i].strip()

            doc = {
                'id': id,
                'author': author,
                'comment': comment
            }
            db.advices.insert_one(doc)
            id = id+1

def set_lunch_data():
    foods = {}
    with open('./lunch.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        id=1
        for i in range(0, len(lines), 2):
            food_name = lines[i+1].strip()
            img = lines[i].strip()

            doc = {
                'id': id,
                'foodname': food_name,
                'img': img
            }
            db.lunchs.insert_one(doc)
            id = id+1


def set_luck_data():
    lucks = {}
    with open('./today_luck.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        id=1
        for i in range(0, len(lines)):
            luck = lines[i].strip()

            doc = {
                'id': id,
                'luck': luck
            }
            db.lucks.insert_one(doc)
            id = id+1


# set_advice_data()
# set_lunch_data()
# set_luck_data()
