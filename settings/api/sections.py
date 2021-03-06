from flask import Flask, jsonify, request, url_for, session, redirect
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongod:27017/notesdb'
api = Api(app)
db = PyMongo(app)
connect = db.db.section
# Section API, gets all sections and adds new section
class AllSections(Resource):
    # connect = db.db.section
    def get(self, user_id):
        # connect = db.db.section
        # sub_sections = connect.find({'subject_id': subject_id})
        sections = []
        for s in connect.find({'user_id': user_id}):
            sections.append({
                'id': str(s['_id']),
                'section': s['section'],
                'subject_id': s['subject_id'],
                'user_id': s['user_id']
                })
        return jsonify({'results': sections})

    def post(self, user_id):
        # connect = db.db.section
        section = request.json['section']
        subject_id = request.json['subject_id']
        connect.insert({'section': section, 'subject_id': subject_id, 'user_id': user_id})
        sections = []
        for s in connect.find({'subject_id': subject_id}):
            sections.append({
                'id': str(s['_id']),
                'section': s['section'],
                'subject_id': s['subject_id'],
                'user_id': user_id
                })
        return jsonify({'success': True, 'results': sections})

# Single section, update and delete subject+
class Section(Resource):
    def get(self, section_id):
        # connect = db.db.section
        section = connect.find_one({'_id': ObjectId(section_id)})
        if section:
            return jsonify({
                'id': str(section['_id']),
                'section': section['section'],
                'subject_id': section['subject_id']
                })
        return jsonify({'results': 'No Section Found'})

    def put(self, section_id):
        # connect = db.db.section
        connect.update_one({'_id': ObjectId(section_id)}, {'$set': {'section': request.json['edit']}}, upsert=False)
        section = connect.find_one({'_id': ObjectId(section_id)})
        return jsonify({'success': True, 'results': {
            'id': str(section['_id']),
            'section': section['section'],
            'subject_id': section['subject_id']
            }})

    def delete(self, section_id):
        # connect = db.db.section
        section = connect.find_one({'_id': ObjectId(section_id)})
        notes = db.db.notes.find({'section_id': section_id})
        flash_cards = db.db.flash_cards.find({'section_id': section_id})
        connect.delete_one(section)
        if notes:
            for n in notes:
                db.db.notes.delete_one(n)
        if flash_cards:
            for f in flash_cards:
                db.db.flash_cards.delete_one(f)
        return jsonify({'result': 'Section Deleted!'})