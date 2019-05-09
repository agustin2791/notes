from flask import Flask, jsonify, request, url_for, session, redirect
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/notesdb'
api = Api(app)
db = PyMongo(app)
connect = db.db.notes

class Notes(Resource):

	def get(self, sub_id, sec_id):
		
		notes = []
		for n in connect.find({'subject_id': sub_id, 'section_id': sec_id}):
			notes.append({
					'id': str(n['_id']),
					'note': n['note'],
					'subject_id': n['subject_id'],
					'section_id': n['section_id']
				})
		return jsonify({'results': notes})

	def post(slef, sub_id, sec_id):
		connect = db.db.notes
