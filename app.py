from flask import Flask, render_template, request, jsonify, make_response
from pymongo import MongoClient
import lunch
import advice
import json

# client = MongoClient('')
# db = client.dbsparta
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def show_home():
   return render_template('index.html')


@app.route('/lunch')
def get_lunch():
    food_name, img = lunch.get_random_lunch()
    data = {
       'foodname': food_name,
       'img': img
    }

    result = make_response(json.dumps(data, ensure_ascii=False, indent=4))
    return result


@app.route('/advice')
def get_advice():
    author, comment = advice.show_random_message()
    data = {
       'author': author,
       'comment': comment
    }

    result = make_response(json.dumps(data, ensure_ascii=False, indent=4))
    return result



if __name__ == '__main__':
   app.run()