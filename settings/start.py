from flask import Flask, jsonify, request, url_for, session, redirect
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
# import bcrypt
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

# app.config['SCRETE_KEY'] = 'thisissecret'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/notesdb'

mongo = PyMongo(app)

class AllSubjects(Resource):
	def get(self):
		connect = mongo.db.subject
		subjects = []
		for c in connect.find():
			subjects.append({'id': str(c['_id']), 'subject': c['subject']})
		return jsonify({'results': subjects})

	def post(self):
		connect = mongo.db.subject
		new_sub = request.json['subject']
		connect.insert({'subject': new_sub})
		return jsonify({'success': True})

class Subject(Resource):
	def get(self, subject_id):
		connect = mongo.db.subject
		subject = connect.find_one({'_id': ObjectId(subject_id)})
		return jsonify({'results': {'id': str(subject['_id']), 'subejct': subject['subject']}})

	def put(self, subject_id):
		connect = mongo.db.subject
		edit = request.json['edit']
		subject = connect.find_one({'_id': ObjectId(subject_id)})
		connect.update_one(subject, {'$set': {'subject': edit}}, upsert=False)
		return jsonify({'id': str(subject['_id']), 'subject': subject['subject']})

	def delete(self, subject_id):
		connect = mongo.db.subject
		subject = connect.find_one({'_id': ObjectId(subject_id)})
		deleted_sub = {'id': str(subject['_id']), 'subject': subject['subject']}
		connect.delete_one(subject)
		return jsonify({'deleted': deleted_sub})


# class HelloWorld(Resource):
# 	def get(self):
# 		return {'about': 'Hello World'}

# 	def post(self):
# 		some_json = request.get_json()
# 		return {'you sent': some_json}, 201

class Api(Resource):
	def get(self, num):
		return {'result': num*10}

api.add_resource(Api, '/api/<int:num>')
api.add_resource(AllSubjects, '/api/subjects')
api.add_resource(Subject, '/api/subjects/<subject_id>')

if __name__ == '__main__':
	app.run(debug=True)