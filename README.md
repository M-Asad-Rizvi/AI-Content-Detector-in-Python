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

bash
cd ai-content-detector
Install dependencies using the requirements.txt file:

bash
pip install -r requirements.txt
Usage
Ensure you have a CSV file with training data named text.csv. The file should contain 'content' and 'label' columns for model training.

Train the model by running the script (you might need to customize it according to your dataset):

bash
python train_model.py
Save the trained model as Ai_Content_Detector.joblib.

Run the Flask application:

bash
python app.py
Open your browser and go to http://localhost:5000/detect?q=YOUR_TEXT_TO_ANALYZE to detect AI-generated content
