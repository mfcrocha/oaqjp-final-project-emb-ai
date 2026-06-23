from EmotionDetection import emotion_detector

# Test cases with expected dominant emotions
def test_emotion_detector():
    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for text, expected_emotion in test_cases.items():
        result = emotion_detector(text)
        dominant_emotion = result["dominant_emotion"]
        
        print(f"Text: {text}")
        print(f"Expected: {expected_emotion}, Got: {dominant_emotion}")
        
        if dominant_emotion == expected_emotion:
            print("PASS\n")
        else:
            print("FAIL\n")

# Run tests
test_emotion_detector()