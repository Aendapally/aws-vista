import json
from flask_cors import CORS
from flask import Flask
from main import res_count
app = Flask(__name__)
CORS(app)


@app.route('/')
def configcall():
    result = res_count()
    return json.dumps(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0")