from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "App for test task"


if __name__ == '__main__':
    app.run(debug=False, port=8080, host="0.0.0.0")
