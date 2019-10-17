from flask import Flask, jsonify, request, url_for, session, redirect
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongod:27017/notesdb'
api = Api(app)
db = PyMongo(app)
connect = db.db.flash_cards

class Cards(Resource):
	def get(self, user_id):
		flash = connect.find({'user_id': user_id})
		flash_cards = []
		for f in flash:
			flash_cards.append({
				'id': str(f['_id']),
				'word': f['word'],
				'def': f['def'],
				'subject_id': f['subject_id'],
				'section_id': f['section_id'],
				'user_id': user_id
				})
		return jsonify({'results': flash_cards})

	def post(self, user_id):
		word = request.json['word']
		deff = request.json['def']
		subject_id = request.json['subject_id']
		section_id = request.json['section_id']

		card = connect.insert({
					'word': word, 
					'def': deff, 
					'subject_id': subject_id, 
					'section_id': section_id, 
					'user_id': user_id})
		return jsonify({'results': {'id': str(card),
									'word': word,
									'def': deff,
									'subject_id': subject_id,
									'section_id': section_id,
									'user_id': user_id}})

class Card(Resource):
	def get(self, card_id):
		card = connect.find_one({'_id': ObjectId(card_id)})
		return jsonify({'results': card})

	def put(self, card_id):
		# card = connect.find_one({'_id': ObjectId(card_id)})
		word = request.json['word']
		deff = request.json['def']

		connect.update_one({'_id': ObjectId(card_id)}, {'$set': {'word': word, 'def': deff}}, upsert=False)
		return jsonify({'updated': True})

	def delete(self, card_id):
		card = connect.find_one({'_id': ObjectId(card_id)})
		connect.delete_one(card)
		return jsonify({'deleted': True})