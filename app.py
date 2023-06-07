from flask import Flask, render_template, request, jsonify, make_response
import randomGetter
import json
import random

app = Flask(__name__)

@app.route('/')
def show_home():
   return render_template('index.html')


@app.route('/lunch')
def get_lunch():
    food_name, img = randomGetter.get_random_lunch()
    data = {
       'foodname': food_name,
       'img': img
    }

    result = make_response(json.dumps(data, ensure_ascii=False, indent=4))
    return result


@app.route('/advice')
def get_advice():
    author, comment = randomGetter.get_random_message()
    data = {
       'author': author,
       'comment': comment
    }

    result = make_response(json.dumps(data, ensure_ascii=False, indent=4))
    return result

def read_luck():
    f = open("today_luck.txt", 'r',encoding='utf-8')
    lines = f.readlines() 
    return lines

luck = read_luck()

@app.route("/luck", methods=["GET"])
def get_luck():
    random_luck = random.sample(luck,3)
    luck_data = {
        'card1': random_luck[0].strip(),
        'card2': random_luck[1].strip(),
        'card3': random_luck[2].strip()
    }
    return jsonify(luck_data)

if __name__ == '__main__':
   app.run()