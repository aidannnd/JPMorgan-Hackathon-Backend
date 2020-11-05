from flask import request
from flask_restplus import Resource
import json

from config import app, api, ns, resource_fields
from logic import User, add_user, delete_user, get_user

@ns.route('/')
class Main(Resource):
    @api.doc(responses={
        201: 'User successfully added.',
        400: 'Adding the user failed.'},
        body=resource_fields)
    def post(self):
        """Adds the provided user to the list and returns the users currently saved"""
        post_json = request.get_json()
        return add_user(post_json)

@ns.route('/<id>')
class Other(Resource):
    @api.doc(responses={
        404: 'User not found',
        200: 'User successfully deleted.',
        500: 'Failed to delete user'},
        params={'id': 'A user id'})
    def delete(self, id):
        """Removes a user based on id"""
        return delete_user(id)

    @api.doc(responses={
        404: 'User not found',
        200: 'User successfully found.',
        500: 'Getting the user failed'},
        params={'id': 'A user id'})
    def get(self, id):
        """Returns the user json based on id"""
        return get_user(id)

if __name__ == '__main__':
    app.run(debug=True)