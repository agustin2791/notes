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
    def get(self):
        # connect = db.db.subject
        subjects = []
        for c in connect.find():
            subjects.append({'id': str(c['_id']), 'subject': c['subject']})
        return jsonify({'results': subjects})

    def post(self):
        # connect = db.db.subject
        new_sub = request.json['subject']
        connect.insert({'subject': new_sub})
        subjects = []
        for c in connect.find():
            subjects.append({'id': str(c['_id']), 'subject': c['subject']})
        return jsonify({'success': True, 'results': subjects})

# Single subject, meant to update and delete subject
class Subject(Resource):
    # connect = db.db.subject
    def get(self, subject_id):
        # connect = db.db.subject
        subject = connect.find_one({'_id': ObjectId(subject_id)})
        return jsonify({'results': {'id': str(subject['_id']), 'subeject': subject['subject']}})

    def put(self, subject_id):
        # connect = db.db.subject
        edit = request.json['edit']
        subject = connect.find_one({'_id': ObjectId(subject_id)})
        connect.update_one({'_id': ObjectId(subject_id)}, {'$set': {'subject': edit}}, upsert=False)
        return jsonify({'id': str(subject['_id']), 'subject': subject['subject']})

    def delete(self, subject_id):
        # connect = db.db.subject
        subject = connect.find_one({'_id': ObjectId(subject_id)})
        deleted_sub = {'id': str(subject['_id']), 'subject': subject['subject']}
        connect.delete_one(subject)
        return jsonify({'deleted': deleted_sub})