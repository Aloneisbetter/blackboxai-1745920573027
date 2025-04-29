from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    """
    Endpoint to accept video file or video URL and return transcription text.
    For demo, returns a mock transcription.
    """
    if 'video' in request.files:
        video_file = request.files['video']
        filename = video_file.filename
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        video_file.save(filepath)
        # Here you would process the video file and transcribe
        transcription = f"Mock transcription for uploaded file: {filename}"
        # Optionally delete the file after processing
        os.remove(filepath)
        return jsonify({'transcription': transcription})
    else:
        data = request.get_json()
        video_url = data.get('videoUrl', '').strip()
        if video_url:
            # Here you would download/process the video from URL and transcribe
            transcription = f"Mock transcription for video URL: {video_url}"
            return jsonify({'transcription': transcription})
        else:
            return jsonify({'error': 'No video file or URL provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
