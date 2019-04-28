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
    },
    {
        'name': 'Competitive Mochi Store',
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
    return jsonify({'Error message': 'Store not found'})


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            stores['name'].append(item)
            return jsonify(new_item)
    return jsonify({'Error message': 'Store not found'})

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'Error message': 'Store not found'})


if __name__ == '__main__':
    app.run(port=5000)
