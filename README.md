# Fake News Detection Using Machine Learning 📰

## Project Overview
Fake News Detection is a machine learning-based web application that identifies whether a given news article is **FAKE** or **REAL**.

The application uses Natural Language Processing (NLP) and a Passive Aggressive Classifier to analyse news text and predict its authenticity.

## Technologies Used
- Python
- Flask
- Machine Learning
- Natural Language Processing (NLP)
- Scikit-learn
- Pandas
- NumPy
- HTML and CSS

## Machine Learning Algorithm
- TF-IDF Vectorization
- Passive Aggressive Classifier
- Train-Test Split

## Features
- User-friendly web interface
- News text input for prediction
- Automatic fake or real news classification
- Machine learning-based prediction

## Model Performance
The project explores multiple classification algorithms, including:
- Passive Aggressive Classifier
- Decision Tree Classifier

## Project Structure
```text
Fake-News-Detection/
│
├── main.py
├── model.pkl
├── templates/
├── static/
└── README.md
```

## How to Run the Project

1. Clone this repository:
   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project folder:
   ```bash
   cd fake-news-detection-ml
   ```

3. Install the required libraries:
   ```bash
   pip install flask scikit-learn pandas numpy
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Open the local URL displayed in the terminal in your browser.

## Dataset

The original news dataset (`news.csv`) is not included because of its file size.

The application uses the pre-trained model (`model.pkl`) and saved TF-IDF vectorizer (`vectorizer.pkl`) to make predictions without requiring the original dataset at runtime.

## Installation

Install the required libraries:

pip install flask scikit-learn

Run the application:

python main.py

## Author
Himavathi YS
