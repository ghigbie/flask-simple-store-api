from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Wonderful Mochi Store',
        'items': [
            {
                'name': 'Mochi',
                'price': '2.50'
            },
            {
                'name': 'Butter Mochi',
                'price': '2.70'
            },
            {
                'name': 'Mango Mochi',
                'price': '2.90'
            }
        ]
    }
]

@app.route('/')
def home():
    return "Yo mochi!"

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return {"Error message": "Store not found : ("} 


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item():
    pass

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return {"Error message": "Items not found : ("}


if __name__ == '__main__':
    app.run(port=5000)
