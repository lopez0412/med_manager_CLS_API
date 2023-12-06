from flask import Blueprint, request, jsonify
from flask_cors import CORS
import traceback


from src.utils.Logger import Logger
from src.models.userModel import User
from src.utils.Security import Security
from src.services.AuthService import AuthService

main = Blueprint('auth_blueprint', __name__)
CORS(main)

@main.route('/', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']

        _user = User(0, username, password, None, None, None)
        authenticated_user = AuthService.login_user(_user)

        if (authenticated_user != None):
            encoded_token = Security.generate_token(authenticated_user)
            return jsonify({'success': True, 'token': encoded_token})
        else:
            response = jsonify({'message': 'Unauthorized'})
            return response, 401
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})
