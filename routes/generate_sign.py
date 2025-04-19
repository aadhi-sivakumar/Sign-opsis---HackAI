from flask import Blueprint, request, jsonify, send_file
from services.sign_avatar_driver import generate_sign_video

generate_sign_bp = Blueprint('generate_sign', __name__)

@generate_sign_bp.route('/generate-sign', methods=['POST'])
def generate_sign():
    data = request.get_json()
    gloss = data.get("gloss")

    if not gloss:
        return jsonify({"error": "No gloss provided"}), 400

    try:
        video_path = generate_sign_video(gloss)
        return send_file(video_path, mimetype='video/mp4')
    except Exception as e:
        return jsonify({"error": str(e)}), 500