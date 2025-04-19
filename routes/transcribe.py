from flask import Blueprint, request, jsonify
from services.speech_to_text import transcribe_audio
import os

transcribe_bp = Blueprint('transcribe', __name__)

@transcribe_bp.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({'error': 'No audio file uploaded'}), 400

    audio_file = request.files['file']
    file_path = os.path.join("data", audio_file.filename)
    audio_file.save(file_path)

    transcript = transcribe_audio(file_path)
    return jsonify({'transcript': transcript})