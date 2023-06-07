from flask import Flask, render_template, request, jsonify, make_response
from pymongo import MongoClient
import lunch
import json

# client = MongoClient('')
# db = client.dbsparta
app = Flask(__name__)

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

   
   

if __name__ == '__main__':
   app.run()