import requests
import json

def emotion_detector(text_to_analyse):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=obj, headers=headers )
    status_code = response.status_code
    if status_code == 400:
        return {"anger": None,"disgust": None,"fear": None,"joy": None,"sadness": None,"dominant_emotion":None}
    
    formatted = json.loads(response.text)
    emotions = get_emotions(formatted)
    dominant_emotion = get_dominant_emotion(emotions)
    emotions["dominant_emotion"] = dominant_emotion
    return emotions

def get_emotions(formatted_json):
    emotions = {"anger": 0,"disgust": 0,"fear": 0,"joy": 0,"sadness": 0}
    emotionPredictions = formatted_json["emotionPredictions"]
    if len(emotionPredictions) == 0:
        return emotions
    emotions = emotionPredictions[0]["emotion"]    
    return emotions

def get_dominant_emotion(emotions):
    dominat = ""
    max_score = 0
    for k, v in emotions.items():
        if v > max_score:
            max_score = v
            dominat = k
    return dominat        
