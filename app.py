from flask import Flask
from flask_cors import CORS

# Import blueprints after initializing Flask app
from routes.transcribe import transcribe_bp
from routes.translate import translate_bp
from routes.generate_sign import generate_sign_bp
from routes.merge_video import merge_bp


# Initialize app
app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(transcribe_bp, url_prefix='/api')
app.register_blueprint(translate_bp, url_prefix='/api')
app.register_blueprint(generate_sign_bp, url_prefix='/api')
app.register_blueprint(merge_bp, url_prefix='/api')

@app.route('/')
def index():
    return {'status': 'SignVision backend running'}

if __name__ == '__main__':
    app.run(debug=True)