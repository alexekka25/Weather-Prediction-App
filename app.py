from flask import Flask, request, render_template
import joblib
import numpy as np

# Load the models and the label encoder
regressor = joblib.load('regressor_model.pkl')
classifier = joblib.load('classifier_model.pkl')
label_encoder = joblib.load('label_encoder (1).pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # A simple HTML form for input

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    input_data = [
        float(request.form['temperature_fahrenheit']),
        float(request.form['feels_like_celsius']),
        float(request.form['temperature_feels_diff']),
        float(request.form['feels_like_fahrenheit']),
        int(request.form['last_updated_day']),
        float(request.form['moonlight_duration']),
        int(request.form['day']),
        int(request.form['moon_illumination']),
        float(request.form['wind_power']),
        float(request.form['daylight_duration'])
    ]
    
    # Convert input data to numpy array and reshape for model
    input_data_array = np.array(input_data).reshape(1, -1)
    
    # Make predictions
    temp_prediction = regressor.predict(input_data_array)[0]
    condition_prediction = classifier.predict(input_data_array)
    condition_prediction_label = label_encoder.inverse_transform(condition_prediction)[0]
    
    return render_template('result.html', 
                           temperature=round(temp_prediction, 1),
                           condition=condition_prediction_label
                           )
                          
if __name__ == '__main__':
    app.run(debug=True)

    