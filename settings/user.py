from flask import Flask, jsonify, request, url_for, session, redirect
from flask.views import MethodView
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/notesdb'
app.config['JWT_SECRET_KEY'] = 'Iy4qLzM1WeHzhJVTbKF0jplDgQS3p8Jl'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=2)
api = Api(app)
db = PyMongo(app)
jwt = JWTManager(app)
flask_bcrypt = Bcrypt(app)

# connect = db.db.section

from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError

user_schema = {
	"type": "object",
	"properties": {
		"first_name": {
			"type": "string"
		},
		"last_name": {
			"type": "string"
		},
		"username": {
			"type": "string"
		},
		"email": {
			"type": "string",
			"format": "email"
		},
		"password": {
			"type": "string",
			"minLength": 6
		}
	},
	"required": ["username", "password"],
	"additionalProperties": False
}

def validate_user(data):
	try:
		validate(data, user_schema)
	except ValidationError as e:
		return {'ok': False, 'message': e}
	except SchemaError as e:
		return {'ok': False, 'message': e}
	return {'ok': True, 'data': data}

class UserRegister(MethodView):
	def post(self):
		data = validate_user(request.get_json())
		if data['ok']:
			data = data['data']
			if db.db.users.find_one({'username': data['username']}) is not None:
				return jsonify({'ok': False, 'message': 'username already exists'}), 400
			if db.db.users.find_one({'email': data['email']}) is not None:
				return jsonify({'ok': False, 'message': 'Email already exists'}), 400
			data['password'] = flask_bcrypt.generate_password_hash(data['password'])
			db.db.users.insert_one(data)
			return jsonify({'ok': True, 'message': 'User created successfully!'}), 200
		else:
			return jsonify({'ok': True, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400

class UserAuth(MethodView):
	def post():
		data = validate_user(request.get_json())
		if data['ok']:
			data = data['data']
			user = db.db.users.find_one({'username': data['username']})
			if user and flask_bcrypt.check_password_hash(user['password'], data['password']):
				del user['password']
				access_token = create_access_token(identity=data)
				refresh_token = create_refresh_token(identity=data)
				user['token'] = access_token
				user['refresh'] = refresh_token
				return jsonify({'ok': True, 'data': user}), 200
			else:
				return jsonify({'ok': False, 'message': 'invalid username or password'}), 401
		else:
			return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400
