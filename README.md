# AI Content Detector  in Python | 99% Accuracy

# AI Content Detector

## Introduction

Welcome to the AI Content Detector project! This application is built using Flask and a pre-trained Support Vector Machine (SVM) model to detect AI-generated content within text input.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-content-detector.git
Change into the project directory:

   ```bash
cd ai-content-detector
Install dependencies using the requirements.txt file:

   ```bash
pip install -r requirements.txt
### Usage
Please make sure you have a CSV file with training data named text.csv. The file should contain 'content' and 'label' columns for model training.
You can use the text.csv file provided in the repo if you don't have this one.



Run the Flask application:

   ```bash
python app.py

By running it will use the pre-trained model as Ai_Content_Detector.joblib.
Open your browser and go to ` http://127.0.0.1:5000/detect?q=Your_Text_To_Analyze ` to detect AI-generated content. And it will give you the output for the given text.

### Example Output:
   ```bash
   
{
  "AI_Sentence_Count": 1,
  "AI_Words": 3,
  "Ai_Written": "95.50%",
  "Ai_sentences": [
    "How are you?"
  ],
  "Human_Written": "4.50%",
  "Input_length": 12,
  "Input_text": "How are you?",
  "Timestamp": "2023-12-23 12:48:27"
}
