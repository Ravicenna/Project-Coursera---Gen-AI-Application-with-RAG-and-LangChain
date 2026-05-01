from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

# ✅ Route utama (biar tidak 404)
@app.route("/")
def home():
    return "Emotion Detection API is running"

# ✅ Route utama untuk tugas
@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    text = request.args.get("textToAnalyze")

    # ❗ Error handling input kosong
    if text is None or text.strip() == "":
        return jsonify({"error": "Invalid input! Please enter text."}), 400

    result = emotion_detector(text)

    # ❗ Error jika API gagal
    if result is None:
        return jsonify({"error": "Error processing request"}), 500

    # 🔥 Ambil emosi dominan
    dominant_emotion = max(result, key=result.get)

    # ✅ Format output sesuai tugas
    return jsonify({
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"],
        "dominant_emotion": dominant_emotion
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)