from flask import Flask, render_template, request
import pickle

with open('../sentiment_analysis.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'text' not in request.form:
        return render_template('index.html', prediction_text = f'No text provided')
    
    user_input = request.form['text']

    prediction = model.predict([user_input])
    sentiment = 'Happy' if prediction == 0 else 'Sad'

    return render_template('index.html', prediction_text = f'The sentiment of the text is: {sentiment}')


if __name__ == "__main__":
    app.run(debug=True)