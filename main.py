
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

loaded_model = pickle.load(open('model.pkl', 'rb'))
tfvect = pickle.load(open('vectorizer.pkl', 'rb'))

def fake_news_det(news):
    vectorized_input_data = tfvect.transform([news])
    prediction = loaded_model.predict(vectorized_input_data)
    return prediction

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    pred = fake_news_det(message)
    print(pred)
    return render_template('index.html', prediction=pred)

if __name__ == '__main__':
    app.run(debug=True)
