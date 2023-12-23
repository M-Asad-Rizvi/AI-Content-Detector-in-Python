# AI Content Detector in Python

## Introduction

Welcome to the AI Content Detector project! This application is built using Flask and a pre-trained Support Vector Machine (SVM) model to detect AI-generated content within text input. The model boasts an accuracy of 99%.

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/M-Asad-Rizvi/AI-Content-Detector-in-Python.git
   ```

2. **Change into the project directory:**
   ```bash
   cd ai-content-detector
   ```

3. **Install dependencies using the requirements.txt file:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Make sure you have a CSV file with training data named `text.csv`. The file should contain 'content' and 'label' columns for model training. You can use the `text.csv` file provided in the repo if you don't have one.

2. **Run the Flask application:**
   ```bash
   python app.py
   ```
   This will use the pre-trained model `Ai_Content_Detector.joblib`.

3. Open your browser and go to `http://127.0.0.1:5000/detect?q=Your_Text_To_Analyze` to detect AI-generated content. The application will provide output for the given text.

### Example Output:

```json
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
```

## File Structure

- **.gitattributes:** Git configuration file.
- **Ai_Content_Detector.joblib:** Pre-trained SVM model.
- **README.md:** Project documentation.
- **app.py:** Flask application for AI content detection.
- **requirements.txt:** List of Python dependencies.
- **text.csv:** CSV file containing training data.



