from flask import Blueprint, request, jsonify, send_file
from services.video_sync import overlay_sign_video

merge_bp = Blueprint('merge', __name__)

@merge_bp.route('/merge-video', methods=['POST'])
def merge():
    data = request.get_json()
    background = data.get("background", "data/original.mp4")
    overlay = data.get("overlay", "data/generated_sign.mp4")

    try:
        merged_path = overlay_sign_video(background, overlay)
        return send_file(merged_path, mimetype='video/mp4')
    except Exception as e:
        return jsonify({'error': str(e)}), 500