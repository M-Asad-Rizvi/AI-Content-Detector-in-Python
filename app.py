from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib
import nltk
from nltk.tokenize import sent_tokenize
from datetime import datetime

nltk.download('punkt')

app = Flask(__name__)


# Load the dataset for model training
df = pd.read_csv('text.csv')

train_data, _, train_labels, _ = train_test_split(
    df['content'],
    df['label'],
    test_size=0.2,
    random_state=42
)

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
train_vectors = tfidf_vectorizer.fit_transform(train_data)

# Load the pre-trained SVM model
loaded_svm_model = joblib.load('Ai_Content_Detector.joblib')

# Function to predict if a string is AI-generated
def predict_ai_generated(input_text, model, vectorizer):
    # Tokenize the input text into sentences
    sentences = sent_tokenize(input_text)

    # Initialize lists to store results
    ai_confidences = []
    ai_sentences = []

    # Process each sentence
    for sentence in sentences:
        # Vectorize the sentence using the TF-IDF vectorizer
        sentence_vector = vectorizer.transform([sentence])

        # Predict the probability of being AI-generated
        probability = model.predict_proba(sentence_vector)[0, 1] * 100

        # Classify the sentence
        predicted_label = model.predict(sentence_vector)[0]

        # Store results for each segment
        if predicted_label == 1:
            ai_confidences.append(probability)
            ai_sentences.append(sentence)

    # Calculate overall confidence percentages
    confidence_percentage = sum(ai_confidences) / len(sentences) if sentences else 0

    # Get the length of the input text
    input_length = len(input_text)

    # Get the length of AI sentences in words
    ai_sentences_word_length = sum(len(sentence.split()) for sentence in ai_sentences)

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Prepare the response
    response = {
        "Input_text": input_text,
        "Input_length": input_length,
        "Human_Written": f"{100 - confidence_percentage:.2f}%",
        "Ai_Written": f"{confidence_percentage:.2f}%",
        "Ai_sentences": [sentence.strip('"') for sentence in ai_sentences],
        "AI_Sentence_Count": len(ai_sentences),
        "AI_Words": ai_sentences_word_length,
        "Timestamp": timestamp,
    }


    return response

@app.route('/detect', methods=['GET'])
def predict():
    # Get the text input from the user as a query parameter
    input_text = request.args.get('q', '')

    # Call the prediction function
    result = predict_ai_generated(input_text, loaded_svm_model, tfidf_vectorizer)

    # Return the results as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
