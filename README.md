# Emotion Detection App

This project is a simple emotion detection application built using Python, Flask, and IBM Watson NLP. It analyzes input text and returns the detected emotions along with the dominant emotion.

## Features

* Detects emotions: anger, disgust, fear, joy, and sadness
* Provides dominant emotion
* REST API built with Flask
* Error handling for invalid input
* Unit testing included

## Project Structure

```
project/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── test_emotion_detection.py
├── server.py
├── requirements.txt
└── README.md
```

## Installation

Install the required dependencies:

```
pip install -r requirements.txt
```

## Running the Application

Start the Flask server:

```
python server.py
```

The server will run at:

```
http://127.0.0.1:5000/
```

## API Usage

Use the following endpoint:

```
/emotionDetector?textToAnalyze=your_text_here
```

### Example:

```
http://127.0.0.1:5000/emotionDetector?textToAnalyze=I am happy
```

### Example Output:

```
{
  "anger": 0.1,
  "disgust": 0.1,
  "fear": 0.1,
  "joy": 0.7,
  "sadness": 0.0,
  "dominant_emotion": "joy"
}
```

## Error Handling

If the input is empty:

```
{
  "error": "Invalid input! Please enter text."
}
```

## Running Tests

Run unit tests using:

```
python test_emotion_detection.py
```

## Static Code Analysis

Run pylint:

```
pip install pylint
pylint server.py
```

## Notes

* The application uses IBM Watson NLP API.
* If the API is unavailable, a fallback response is used to ensure the application continues to work.

## Author

This project was developed as part of a Coursera assignment on building AI-powered applications.
