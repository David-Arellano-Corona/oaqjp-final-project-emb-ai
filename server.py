from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detector():
    text_to_analyse = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyse)
    
    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return f"""
    For the given statement, the system response is 
    'anger': {emotions['anger']}, 
    'disgust': {emotions['disgust']}, 
    'fear': {emotions["fear"]}, 
    'joy': {emotions['joy']} and 
    'sadness': {emotions['sadness']}. 
    The dominant emotion is {emotions['dominant_emotion']}.
    """

@app.route("/")
def render_page():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")