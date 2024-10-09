from flask import Flask, jsonify, request, session, make_response
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os

from models import db, User

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_key_for_dev')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

bcrypt = Bcrypt(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/data')
def get_data():
    data = {'message': 'Hello from the backend!'}
    return jsonify(data)

@app.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)