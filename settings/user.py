from flask import Flask, jsonify, request, url_for, session, redirect
from flask.views import MethodView
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager, jwt_refresh_token_required, jwt_required, create_access_token, create_refresh_token
from flask_cors import cross_origin
from flask_bcrypt import Bcrypt
from bson.objectid import ObjectId
from base64 import b64decode
import json
import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongod:27017/notesdb'
app.config['JWT_SECRET_KEY'] = '0rgFhiQ7vrgEOaoU5NnY_ZCommoZgelFKa1dxGc0TK3b_KwNIKeTaSTjOVNWjm_38WArirTrmmhY8DSg8OPC6hvCw62X0DaRxZVCW8Z-fVJeJdX005R6oVlCxMES1aAT_3RYDWiMf-Dv9dF0-uhgZq48yumOYYObpGQ8jlJ_g5M5Lm0oLgHb_LVUhE8cpgshER4OZkLu5pR49X_gynKFxjC2tRTn886-vry3NFzM1yFmz3bja_RGj8cW07RbfjIEr9O4ieRr5rXzYNGtoSeix19jOPEsOpE4_HDbOKOosHnr2qZl3Q4M4gKbsyLvovD4TnNJ7piI7ua4TDB40qfuuw'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=2)
app.config['JWT_ALGORITHM'] = 'HS256'
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

def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    # try:
    tokenParts = auth_token.split('.')
    tokenPayload = b64decode(tokenParts[1])
    jsonPayload = json.loads(tokenPayload)
    return jsonPayload['identity']['username']
    # except jwt.ExpiredSignatureError:
    #     return 'Signature expired. Please log in again.'
    # except:
    #     return
class UserRegister(MethodView):
	def post(self):
		data = validate_user(request.get_json())
		if data['ok']:
			password = data['data']['password']
			data = data['data']
			if db.db.users.find_one({'username': data['username']}) is not None:
				return jsonify({'ok': False, 'message': 'username already exists'}), 400
			if db.db.users.find_one({'email': data['email']}) is not None:
				return jsonify({'ok': False, 'message': 'Email already exists'}), 400
			data['password'] = flask_bcrypt.generate_password_hash(data['password'])
			db.db.users.insert_one(data)
			data['_id'] = str(data['_id'])
			data['password'] = password
			return jsonify({'ok': True, 'data': data}), 200
		else:
			return jsonify({'ok': True, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400

class UserAuth(MethodView):
	# decorators = [cross_origin]
	def post(self):
		data = validate_user(request.get_json())
		expires = datetime.timedelta(days=7)
		if data['ok']:
			data = data['data']
			username = data['username']
			if '@' in username:
				user = db.db.users.find_one({'email': username})
			else:
				user = db.db.users.find_one({'username': data['username']})
			if user and flask_bcrypt.check_password_hash(user['password'], data['password']):
				del user['password']
				access_token = create_access_token(identity=data, expires_delta=expires)
				refresh_token = create_refresh_token(identity=data, expires_delta=expires)
				user['token'] = access_token
				user['refresh'] = refresh_token
				user['_id'] = str(user['_id'])
				return jsonify({'ok': True, 'data': user}), 200
			else:
				return jsonify({'ok': False, 'message': 'invalid username or password'}), 401
		else:
			return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400

class User(MethodView):
	decorators = [jwt_required]
	def get(self):
		auth = request.headers.get('Authorization')
		if auth:
			token = auth.split(' ')[1]
		else:
			token = None
		if token:
			resp = decode_auth_token(token)
			print('id: ', resp)
			if '@' in resp:
				data = db.db.users.find_one({'email': resp})
			else:
				data = db.db.users.find_one({'username': resp })
			del data['password']
			data['_id'] = str(data['_id'])
			return jsonify({'ok': True, 'data': data}), 200
		return jsonify({'msg': 'No Token provided'})