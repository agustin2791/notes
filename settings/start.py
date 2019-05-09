from flask import Flask, jsonify, request, url_for, session, redirect
from flask_restful import Resource, Api
from flask_pymongo import PyMongo, MongoClient
from flask_user import login_required, UserManager, UserMixin
import bcrypt
from bson.objectid import ObjectId
from api.subjects import AllSubjects, Subject
from api.sections import AllSections, Section

# app = Flask(__name__)
# api = Api(app)

# app.config['SCRETE_KEY'] = 'Iy4qLzM1WeHzhJVTbKF0jplDgQS3p8Jl'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/notesdb'
# db = MongoEngine(app)

class ConfigClass(object):
	SECRET_KEY = 'Iy4qLzM1WeHzhJVTbKF0jplDgQS3p8Jl'
	MONGO_URI = 'mongodb://localhost:27017/notesdb'
	USER_APP_NAME = 'Notes App'
	USER_ENABLE_EMAIL = False
	USER_ENABLE_USERNAME = True
	USER_REQUIRE_RETYPE_PASSWORD = False

# class Api(Resource):
# 	def get(self, num):
# 		return {'result': num*10}

def start_app():
	app = Flask(__name__)
	app.config.from_object(__name__+'.ConfigClass')
	api = Api(app)
	db = PyMongo(app)

	# class User(db.Document, UserMixin):
	# 	meta = {'collection': 'admin'}
	# 	active = db.BooleanField(default=True)
	# 	email = db.StringField(max_length=50)
	# 	password = db.StringField()

	# user_manager = UserManager(app, db, User)

	# api.add_resource(Api, '/api/<int:num>')
	api.add_resource(AllSubjects, '/api/subjects')
	api.add_resource(Subject, '/api/subjects/<subject_id>')
	api.add_resource(AllSections, '/api/sections/<subject_id>')
	api.add_resource(Section, '/api/section/<section_id>')

	return app

if __name__ == '__main__':
	app = start_app()
	app.run(debug=True)
