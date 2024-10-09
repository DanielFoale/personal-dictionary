from flask import Flask, jsonify, request, session, make_response
from flask_jwt_extended import JWTManager, create_access_token
from flask_migrate import Migrate
from flask_cors import CORS
from flask_bcrypt import Bcrypt
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
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

@app.route('/')
def hello_world():
    users = User.query.filter_by(username='tim').first()
    if users==None:
        return 'error'

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

@app.route('/api/register', methods=['POST'])
def register():
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    if not username or not password:
        return jsonify({"message": "Username and password are required"})
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"message": "Username is already taken"})
    new_user = User(username=username, password=bcrypt.generate_password_hash(password).decode('utf-8'))
    db.session.add(new_user)
    db.session.commit()
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials"})

if __name__ == '__main__':
    app.run(port=5555, debug=True)