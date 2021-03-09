from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import marshmallow
import os

# Init app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': "Hello World"})


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
