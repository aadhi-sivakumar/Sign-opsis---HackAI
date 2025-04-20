from flask import Flask, request, jsonify
from speech_to_text import audio_to_asl
import os

app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def audio_to_asl():
    file_path = request.files['file_path']
    if os.path.exists(file_path):
        audio_to_asl(file_path)
        return jsonify({'status': True, 'message': 'Success'}), 200 
    else:
        return jsonify({'status': False, 'message': 'Invalid file path'}), 400
    
if __name__ == '__main__':
    app.run(debug=True)
