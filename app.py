from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import lunch

# client = MongoClient('')
# db = client.dbsparta
app = Flask(__name__)

@app.route('/')
def show_home():
   return render_template('index.html')

@app.route('/lunch')
def get_lunch():
   food_name, img = lunch.get_random_lunch()

   
   

if __name__ == '__main__':
   app.run()