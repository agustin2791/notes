from flask import Flask, jsonify, request, url_for, session, redirect
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
# from flask_pymongo import PyMongo, MongoClient
from flask_user import login_required, UserManager, UserMixin
import bcrypt
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)

# app.config['SCRETE_KEY'] = 'Iy4qLzM1WeHzhJVTbKF0jplDgQS3p8Jl'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/notesdb'
db = MongoEngine(app)

class ConfigClass(object):
	SECRET_KEY = 'Iy4qLzM1WeHzhJVTbKF0jplDgQS3p8Jl'
	MONGODB_SETTINGS = {
		'db': 'notesdb',
		'host': 'mongodb://localhost:27017/notesdb'
	}
	USER_APP_NAME = 'Notes App'
	USER_ENABLE_EMAIL = False
	USER_ENABLE_USERNAME = True
	USER_REQUIRE_RETYPE_PASSWORD = False

class User(db.Document, UserMixin):
	meta = {'collection': 'admin'}
	active = db.BooleanField(default=True)
	email = db.StringField(max_length=50)
	password = db.StringField()

app.config.from_object(__name__+'.ConfigClass')
user_manager = UserManager(app, db, User)

# Subject API, gets all subjects and posts new
class AllSubjects(Resource):
	def get(self):
		connect = db.db.subject
		subjects = []
		for c in connect.find():
			subjects.append({'id': str(c['_id']), 'subject': c['subject']})
		return jsonify({'results': subjects})

	def post(self):
		connect = db.db.subject
		new_sub = request.json['subject']
		connect.insert({'subject': new_sub})
		subjects = []
		for c in connect.find():
			subjects.append({'id': str(c['_id']), 'subject': c['subject']})
		return jsonify({'success': True, 'results': subjects})

# Single subject, meant to update and delete subject
class Subject(Resource):
	def get(self, subject_id):
		connect = db.db.subject
		subject = connect.find_one({'_id': ObjectId(subject_id)})
		return jsonify({'results': {'id': str(subject['_id']), 'subeject': subject['subject']}})

	def put(self, subject_id):
		connect = db.db.subject
		edit = request.json['edit']
		subject = connect.find_one({'_id': ObjectId(subject_id)})
		connect.update_one({'_id': ObjectId(subject_id)}, {'$set': {'subject': edit}}, upsert=False)
		return jsonify({'id': str(subject['_id']), 'subject': subject['subject']})

	def delete(self, subject_id):
		connect = db.db.subject
		subject = connect.find_one({'_id': ObjectId(subject_id)})
		deleted_sub = {'id': str(subject['_id']), 'subject': subject['subject']}
		connect.delete_one(subject)
		return jsonify({'deleted': deleted_sub})

# Section API, gets all sections and adds new section
class AllSections(Resource):
	def get(self, subject_id):
		connect = db.db.section
		# sub_sections = connect.find({'subject_id': subject_id})
		sections = []
		for s in connect.find({'subject_id': subject_id}):
			sections.append({
				'id': str(s['_id']),
				'section': s['section'],
				'subject_id': s['subject_id']
				})
		return jsonify({'results': sections})

	def post(self, subject_id):
		connect = db.db.section
		section = request.json['section']
		connect.insert({'section': section, 'subject_id': subject_id})
		sections = []
		for s in connect.find({'subject_id': subject_id}):
			sections.append({
				'id': str(s['_id']),
				'section': s['section'],
				'subject_id': s['subject_id']
				})
		return jsonify({'success': True, 'results': sections})

# Single section, update and delete subject+
class Section(Resource):
	def get(self, section_id):
		connect = db.db.section
		section = connect.find_one({'_id': ObjectId(section_id)})
		if section:
			return jsonify({
				'id': str(section['_id']),
				'section': section['section'],
				'subject_id': section['subject_id']
				})
		return jsonify({'results': 'No Section Found'})

	def put(self, section_id):
		connect = db.db.section
		connect.update_one({'_id': ObjectId(section_id)}, {'$set': {'section': request.json['edit']}}, upsert=False)
		section = connect.find_one({'_id': ObjectId(section_id)})
		return jsonify({'success': True, 'results': {
			'id': str(section['_id']),
			'section': section['section'],
			'subject_id': section['subject_id']
			}})

	def delete(self, section_id):
		connect = db.db.section
		section = connect.find_one({'_id', ObjectId(section_id)})
		connect.delete_one(section)
		return jsonify({'result': 'Section Deleted!'})

class Api(Resource):
	def get(self, num):
		return {'result': num*10}

api.add_resource(Api, '/api/<int:num>')
api.add_resource(AllSubjects, '/api/subjects')
api.add_resource(Subject, '/api/subjects/<subject_id>')
api.add_resource(AllSections, '/api/sections/<subject_id>')
api.add_resource(Section, '/api/section/<section_id>')

if __name__ == '__main__':
	app.run(debug=True)
