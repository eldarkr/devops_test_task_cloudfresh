import os
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Test task for Cloudfresh"


if __name__ == '__main__':
    load_dotenv()
    port = int(os.getenv("PORT"))
    host = os.getenv("HOST")
    debug = os.getenv("DEBUG")

    app.run(debug=debug, port=port, host=host)
