from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from schemas.trivia_schema import trivia_schema, trivia_schemas
from models import db, Trivia

trivia_bp = Blueprint('trivia', __name__)

# Get all trivia collections
@trivia_bp.route('/trivia', methods=['GET'])
@login_required
def get_trivia_collections():
    trivia = Trivia.query.filter_by(user_id=current_user.id).all()
    result = trivia_schemas.dump(trivia)
    return jsonify(result), 200

# Get details of a specific trivia collection
@trivia_bp.route('/trivia/<int:trivia_id>', methods=['GET'])
@login_required
def get_trivia_collection(trivia_id):
    trivia = Trivia.query.filter_by(id=trivia_id, user_id=current_user.id).first()
    if not trivia:
        return jsonify(message='Trivia collection not found'), 404
    result = trivia_schema.dump(trivia)
    return jsonify(result), 200

# Create a new trivia collection
@trivia_bp.route('/trivia', methods=['POST'])
@login_required
def create_trivia_collection():
    category = request.json.get('category')
    question = request.json.get('question')
    answer = request.json.get('answer')

    new_trivia = Trivia(category=category, question=question, answer=answer, user_id=current_user.id)
    db.session.add(new_trivia)
    db.session.commit()

    result = trivia_schema.dump(new_trivia)
    return jsonify(result), 201

# Update a trivia collection
@trivia_bp.route('/trivia/<int:trivia_id>', methods=['PUT'])
@login_required
def update_trivia_collection(trivia_id):
    trivia = Trivia.query.filter_by(id=trivia_id, user_id=current_user.id).first()
    if not trivia:
        return jsonify(message='Trivia collection not found'), 404

    trivia.category = request.json.get('category', trivia.category)
    trivia.question = request.json.get('question', trivia.question)
    trivia.answer = request.json.get('answer', trivia.answer)
    db.session.commit()

    result = trivia_schema.dump(trivia)
    return jsonify(result), 200

# Delete a trivia collection
@trivia_bp.route('/trivia/<int:trivia_id>', methods=['DELETE'])
@login_required
def delete_trivia_collection(trivia_id):
    trivia = Trivia.query.filter_by(id=trivia_id, user_id=current_user.id).first()
    if not trivia:
        return jsonify(message='Trivia collection not found'), 404

    db.session.delete(trivia)
    db.session.commit()

    return jsonify(message='Trivia collection deleted'), 200

