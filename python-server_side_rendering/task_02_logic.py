import json

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route('/items', methods=['GET'])
def items():
    with open("items.json", 'r') as json_file:
        data = json.load(json_file)
        items = data['items']
    return render_template("items.html", items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)