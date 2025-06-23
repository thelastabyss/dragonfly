# src/app.py

from flask import Flask, render_template, request
from src.utils.paths import SONG_JSON_PATH, OUTPUT_DIR, FEEDBACK_DATA_PATH
from src.utils.user_to_vector import compute_user_feature_dict
from src.logic.similarity import get_recommended_songs
import json
import os
import uuid
from flask import request, redirect, render_template, send_file


app = Flask(__name__)

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    session_id = str(uuid.uuid4())  # each playlist is one session
    user_inputs = {
        "mood_happy_low": float(request.form["mood_happy_low"]),
        "mood_anxious_peaceful": float(request.form["mood_anxious_peaceful"]),
        "mood_energetic_tired": float(request.form["mood_energetic_tired"]),
        "mental_clarity": float(request.form["mental_clarity"])
    }
    
    user_feature_dict = compute_user_feature_dict(user_inputs)
    
    print("User vector input raw:", request.form)
    print("User vector after normalisation:", user_feature_dict)

    top_songs = get_recommended_songs(user_feature_dict)

    return render_template("results.html",
                            songs=top_songs,
                            session_id=session_id,
                            user_vector=user_feature_dict,
                            track_ids=[song["track_id"] for song in top_songs])

from datetime import datetime
import csv

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    feedback_data = {
        "session_id": request.form["session_id"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "match_mood": request.form["match_mood"],
        "reuse": request.form["reuse"],
        "comments": request.form["comments"],
        "recommended_track_ids": request.form["track_ids"],
        "user_vector": request.form["user_vector"]
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_exists = os.path.isfile(FEEDBACK_DATA_PATH)

    with open(FEEDBACK_DATA_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=feedback_data.keys())

        if not file_exists:
            writer.writeheader()
        print(feedback_data)
        writer.writerow(feedback_data)
        

    # Return same results page without changes
    return "", 204  # No Content (JS will handle hiding form and showing thank you)


@app.route("/download_feedback")
def download_feedback():
    return send_file(FEEDBACK_DATA_PATH, as_attachment=True)



#if __name__ == "__main__":
#    app.run(debug=True)
