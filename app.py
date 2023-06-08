from flask import Flask, render_template, request, jsonify, make_response
import randomGetter
import json

app = Flask(__name__)

@app.route('/')
def show_home():
   return render_template('index.html')


@app.route('/lunch')
def get_lunch():
    random_results = randomGetter.get_random_lunch()
    
    data = []
    for food_name, img in random_results:
        data.append({
            'foodname': food_name,
            'img': img
        })

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


@app.route("/luck", methods=["GET"])
def get_luck():
    card1, card2, card3 = randomGetter.get_random_luck()
    luck_data = {
        'card1': card1.strip(),
        'card2': card2.strip(),
        'card3': card3.strip()
    }
    return jsonify(luck_data)

if __name__ == '__main__':
   app.run()