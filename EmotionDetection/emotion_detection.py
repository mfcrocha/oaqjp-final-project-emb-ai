import requests
import json

def emotion_detector(text_to_analyze):
    # API endpoint for emotion detection
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Required headers to access the model
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON structure with the text to analyze
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Send POST request to the API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convert response text into a Python dictionary
    response_dict = json.loads(response.text)
    
    # Extract emotion scores from the response
    emotions = response_dict['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Determine the dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return the formatted output as required
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }