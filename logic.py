from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from config import users_ref
from flask import request, jsonify
import random, string

def generate_id():
    # creates the id for the user
    ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(28))

@dataclass_json
@dataclass
class User:
    name: str
    email: str
    phone: str
    city: str
    categories: List[str]
    events: List[str]
    
def add_user(post_json):
    try:
        # add the a document with id from generate_id() to the Users collection
        users_ref.document(generate_id()).set(request.json)
        return 'User successfully added.', 201

    except:
        return 'Adding the user failed.', 400

def delete_user(id):
    try:
        if users_ref.document(id).get().exists:
            users_ref.document(id).delete() # delete user
            return 'User successfully deleted.', 200
        else:
            return 'User not found.', 404
    except:
        return 'Failed to delete user', 500

def get_user(id):
    try:
        if users_ref.document(id).get().exists:
            # get the user as DocumentSnapshot and convert it to a dict
            user_json = users_ref.document(id).get().to_dict() 
            return user_json, 200
        else:
            return 'User not found.', 404

    except:
        return 'Getting the user failed', 500