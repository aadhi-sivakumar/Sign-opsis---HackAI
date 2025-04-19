from flask import Blueprint, request, jsonify

translate_bp = Blueprint('translate', __name__)

@translate_bp.route('/translate', methods=['POST'])
def translate():
    # Dummy logic for testing
    return jsonify({'gloss': 'HELLO MY NAME SHIRAM'})