from flask import Blueprint, request, jsonify
from src.models.user import User, db
from src.services.auth_service import create_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = create_user(data['username'], data['password'])
    return jsonify({'message': 'User created successfully!'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = authenticate_user(data['username'], data['password'])
    return jsonify({'token': token}), 200