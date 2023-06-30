from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash
from schemas.user_schema import user_schema
from models import db, User

users_bp = Blueprint('users', __name__)

# User registration
@users_bp.route('/register', methods=['POST'])
def register():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')

    # Check if email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify(message='Email already exists'), 409

    # Create a new user
    new_user = User(name=name, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    result = user_schema.dump(new_user)
    return jsonify(result), 201

# User login
@users_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify(message='Invalid email or password'), 401

    # Log in the user
    login_user(user)

    result = user_schema.dump(user)
    return jsonify(result), 200

# User logout
@users_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify(message='Logged out'), 200

# Get the currently logged in user
@users_bp.route('/user', methods=['GET'])
@login_required
def get_user():
    result = user_schema.dump(current_user)
    return jsonify(result), 200

