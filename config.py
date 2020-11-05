from flask import Flask
from flask_restplus import Api, fields
from firebase_admin import credentials, firestore, initialize_app

# RestPLUS configuration
app = Flask(__name__)
api = Api(app, version='1.0', title='User Information',
          description='A representation of user information')

ns = api.namespace('users', description='Access and manipulate information about users')

# Serializers
resource_fields = api.model('User', {'name': fields.String, 'email': fields.String, 'phone': fields.String,
'city': fields.String, 'interests': fields.List(fields.String), 'events': fields.List(fields.String)})

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
users_ref = db.collection('Users')