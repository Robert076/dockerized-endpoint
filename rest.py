from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>The API is working</h1>'

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port='5000')
