form flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Yo mochi!"

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store')
def get_store():
    pass

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item():
    pass

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

app.run(port=5000)
