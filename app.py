form flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Yo mochi!"

app.run(port=5000)
