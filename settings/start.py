from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)

app.config['SCRETE_KEY'] = 'thisissecret'
app.config['MONGO_URI'] = 'mongodb://localhost:61297/notedb'
db = PyMongo(app)

class HelloWorld(Resource):
	def get(self):
		return {'about': 'Hello World'}

	def post(self):
		some_json = request.get_json()
		return {'you sent': some_json}, 201

class Api(Resource):
	def get(self, num):
		return {'result': num*10}

api.add_resource(HelloWorld, '/')
api.add_resource(Api, '/api/<int:num>')

if __name__ == '__main__':
	app.run(debug=True)