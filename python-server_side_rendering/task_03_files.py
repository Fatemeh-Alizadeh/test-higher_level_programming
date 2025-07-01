import csv
import json

import requests
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
        items = data.get('items', [])
    return render_template("items.html", items=items), 200

def read_json():
    try:
        with open("products.json", 'r') as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print(e)
        return []

def read_csv():
    products = []
    try:
        with open("products.csv", 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                products.append({
                    'id': row['id'],
                    'name': row['name'],
                    'category': row['category'],
                    'price': row['price']
                })
    except Exception as e:
        print(e)
        return []
    return products



@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    if source == 'json':
        product_list = read_json()
    elif source == 'csv':
        product_list = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source"),400

    if product_id:
        filtered = [p for p in product_list if int(p['id']) == product_id]
        print(product_list)
        if not filtered:
            return render_template('product_display.html', error="Product not found"), 404
        product_list = filtered


    return render_template('product_display.html', products=product_list), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)