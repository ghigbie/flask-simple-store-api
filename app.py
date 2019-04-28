from flask import Flask, jsonify

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
    pass

@app.route('/store/<string:name>')
def get_store(name):
    return {
        'requestedStore': stores
    }

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item():
    pass

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


if __name__ == '__main__':
    app.run(port=5000)
