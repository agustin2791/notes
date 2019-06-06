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

	def get(self, user_id):
		notes = []
		for n in connect.find({'user_id': user_id}):
			notes.append({
					'id': str(n['_id']),
					'note': n['note'],
					'subject_id': n['subject_id'],
					'section_id': n['section_id'],
					'user_id': user_id
				})
		return jsonify({'results': notes})

	def post(slef, user_id):
		sub_id = request.json['subject_id']
		sec_id = request.json['section_id']
		note = request.json['note']
		new_note = connect.insert({'note': note, 'subject_id': sub_id, 'section_id': sec_id, 'user_id': user_id})
		print new_note
		return_note = {
			'id': str(new_note),
			'note':  note,
			'subject_id': sub_id,
			'section_id': sec_id,
			'user_id': user_id
		}
		return jsonify({'results': return_note})

class Note(Resource):
	def get(self, note_id):
		note = connect.find_one({'_id': ObjectId(note_id)})
		note['_id'] = str(note['_id'])
		return jsonify({'results': note})

	def put(self, note_id):
		update_note = request.json['note']
		note = connect.find_one({'_id': ObjectId(note_id)})
		connect.update_one({'_id': ObjectId(note_id)}, {'$set': {'note': update_note}}, upsert=False)
		return jsonify({'updated': True})

	def delete(self, note_id):
		note = connect.find_one({'_id': ObjectId(note_id)})
		connect.delete_one(note)
		return jsonify({'deleted': True})

