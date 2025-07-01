from flask import Flask, request, jsonify, send_from_directory
from summarize import generate_summary
from tts import generate_tts_audio_and_subs
from render import generate_video
import os

app = Flask(__name__)

@app.route("/api/summarize", methods=["POST"])
def summarize_route():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    summary = generate_summary(text)
    audio_path, subtitle_path = generate_tts_audio_and_subs(summary)
    video_path = generate_video(summary, audio_path)

    return jsonify({
        "summary": summary,
        "video": f"/static/{os.path.basename(video_path)}",
        "audio": f"/static/{os.path.basename(audio_path)}",
        "subtitles": f"/static/{os.path.basename(subtitle_path)}"
    })

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
