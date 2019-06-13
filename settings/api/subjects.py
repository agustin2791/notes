from flask import Flask, jsonify, request, url_for, session, redirect
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/notesdb'
api = Api(app)
db = PyMongo(app)
connect = db.db.subject

class AllSubjects(Resource):
    # connect = db.db.subject
    def get(self, user_id):
        # connect = db.db.subject
        subject = connect.find({'user_id': user_id})
        pretty_subjects = []
        for s in subject:
            pretty_subjects.append({
                'id': str(s['_id']),
                'subject': s['subject'],
                'user_id': s['user_id']
                })
        return jsonify({'results': {'subject': pretty_subjects}})

    def post(self, user_id):
        # connect = db.db.subject
        new_sub = request.json['subject']
        print user_id
        connect.insert({'subject': new_sub, 'user_id': user_id})
        subjects = []
        for c in connect.find({'user_id': user_id}):
            subjects.append({'id': str(c['_id']), 'subject': c['subject'], 'user_id': c['user_id']})
        return jsonify({'success': True, 'results': subjects})

# Single subject, meant to update and delete subject
class Subject(Resource):
    # connect = db.db.subject
    def get(self, subject_id):
        subject = request.json['subject_id']
        data = connect.find_one({'_id': ObjectId(subject_id)})
        data['_id'] = str(data['_id'])
        return jsonify({'results': {'subject': data}})

    def put(self, subject_id):
        # connect = db.db.subject
        edit = request.json['edit']
        subject = connect.find_one({'_id': ObjectId(subject_id)})
        connect.update_one({'_id': ObjectId(subject_id)}, {'$set': {'subject': edit}}, upsert=False)
        return jsonify({'id': str(subject['_id']), 'subject': edit})

    def delete(self, subject_id):
        # connect = db.db.subject
        subject = connect.find_one({'_id': ObjectId(subject_id)})
        sections = db.db.section.find({'subject_id': subject_id})
        notes = db.db.notes.find({'subject_id': subject_id})
        flash = db.db.flash_cards.find({'subject_id': subject_id})
        
        deleted_sub = {'id': str(subject['_id']), 'subject': subject['subject']}
        connect.delete_one(subject)
        if sections:
            for s in sections:
                db.db.section.delete_one(s)
        if notes:
            for n in notes:
                db.db.notes.delete_one(n)
        if flash:
            for f in flash:
                db.db.flash_cards.delete_one(f)
        return jsonify({'deleted': deleted_sub})