def emotion_detector(text_to_analyze):

    text = text_to_analyze.lower()

    if "happy" in text or "great" in text:
        dominant = "joy"
        joy = 0.95
        anger = 0.01
        disgust = 0.01
        fear = 0.01
        sadness = 0.02

    elif "sad" in text:
        dominant = "sadness"
        joy = 0.01
        anger = 0.01
        disgust = 0.01
        fear = 0.05
        sadness = 0.92

    elif "angry" in text:
        dominant = "anger"
        joy = 0.01
        anger = 0.90
        disgust = 0.03
        fear = 0.03
        sadness = 0.03

    else:
        dominant = "neutral"
        joy = 0.20
        anger = 0.20
        disgust = 0.20
        fear = 0.20
        sadness = 0.20

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant
    }