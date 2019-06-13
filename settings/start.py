from flask import Flask, jsonify, request, url_for, session, redirect, render_template
from flask_restful import Resource, Api
from flask_pymongo import PyMongo, MongoClient
from flask_user import login_required, UserManager, UserMixin
from flask_jwt_extended import JWTManager, jwt_refresh_token_required
from flask_cors import CORS
import bcrypt
from bson.objectid import ObjectId
from api.subjects import AllSubjects, Subject
from api.sections import AllSections, Section
from api.notes import Notes, Note
from api.flash_cards import Cards, Card
from user import UserRegister, UserAuth, User
import datetime
# app = Flask(__name__)
# api = Api(app)

# app.config['SCRETE_KEY'] = 'Iy4qLzM1WeHzhJVTbKF0jplDgQS3p8Jl'
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/notesdb'
# db = MongoEngine(app)

class ConfigClass(object):
	
	MONGO_URI = 'mongodb://localhost:27017/notesdb'
	USER_APP_NAME = 'Notes App'
	USER_ENABLE_EMAIL = False
	USER_ENABLE_USERNAME = True
	USER_REQUIRE_RETYPE_PASSWORD = False
	JWT_SECRET_KEY = '0rgFhiQ7vrgEOaoU5NnY_ZCommoZgelFKa1dxGc0TK3b_KwNIKeTaSTjOVNWjm_38WArirTrmmhY8DSg8OPC6hvCw62X0DaRxZVCW8Z-fVJeJdX005R6oVlCxMES1aAT_3RYDWiMf-Dv9dF0-uhgZq48yumOYYObpGQ8jlJ_g5M5Lm0oLgHb_LVUhE8cpgshER4OZkLu5pR49X_gynKFxjC2tRTn886-vry3NFzM1yFmz3bja_RGj8cW07RbfjIEr9O4ieRr5rXzYNGtoSeix19jOPEsOpE4_HDbOKOosHnr2qZl3Q4M4gKbsyLvovD4TnNJ7piI7ua4TDB40qfuuw'
	JWT_ALGORITHM = 'HS256'

# class Api(Resource):
# 	def get(self, num):
# 		return {'result': num*10}

def start_app():
	app = Flask(__name__,
				static_folder="../dist/static",
				template_folder="../dist")
	app.config.from_object(__name__+'.ConfigClass')
	api = Api(app)
	db = PyMongo(app)
	jwt = JWTManager(app)
	cors = CORS(app)
	# cors = CORS(app, origins=["http://127.0.0.1:8080","http://localhost:8080"], allow_headers=[
 #    	"Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
 #    	supports_credentials=True)


	# class User(db.Document, UserMixin):
	# 	meta = {'collection': 'admin'}
	# 	active = db.BooleanField(default=True)
	# 	email = db.StringField(max_length=50)
	# 	password = db.StringField()

	# user_manager = UserManager(app, db, User)

	# api.add_resource(Api, '/api/<int:num>')
	api.add_resource(AllSubjects, '/api/subjects/<user_id>')
	api.add_resource(Subject, '/api/subjects/subject/<subject_id>')
	api.add_resource(AllSections, '/api/sections/<user_id>')
	api.add_resource(Section, '/api/sections/section/<section_id>')
	api.add_resource(Notes, '/api/notes/<user_id>')
	api.add_resource(Note, '/api/notes/note/<note_id>')
	api.add_resource(Cards, '/api/flash_cards/<user_id>')
	api.add_resource(Card, '/api/flash_cards/flash_card/<card_id>')
	app.add_url_rule('/auth/register', view_func=UserRegister.as_view('userregister'))
	app.add_url_rule('/auth/login', view_func=UserAuth.as_view('userauth'))
	app.add_url_rule('/auth/user', view_func=User.as_view('user'))

	@app.route('/refresh', methods=['POST'])
	@jwt_refresh_token_required
	def refresh():
		current_user = get_jwt_identity()
		ret = {
			'token': create_access_token(identity=current_user)
		}
		return jsonify({'ok': True, 'data': ret}), 200

	@app.route('/', defaults={'path': ''})
	@app.route('/<path:path>')
	def catch_all(path):
		return render_template("index.html")



	return app

if __name__ == '__main__':
	app = start_app()
	app.run(debug=False)
