# World Weather Repository - Weather Prediction Project

![Weather Prediction Homepage](temp.jpg)

Welcome to the World Weather Repository, a comprehensive weather prediction system designed to forecast temperature and provide weather conditions using cutting-edge machine learning models.

# Project Overview

This project is focused on predicting the temperature in Celsius and displaying corresponding weather conditions, such as "Sunny," "Partly Cloudy," and "Light Drizzle," among others. By combining historical weather data with advanced machine learning techniques, we aim to provide users with reliable and real-time weather insights.

## Key Features

* Temperature Prediction: Predicts the temperature in Celsius with high accuracy.

* Weather Condition Display: Shows the predicted weather condition (e.g., Sunny, Partly Cloudy).

* Interactive User Interface: Allows users to input relevant features and receive instant predictions via a Flask web application.

* Model Optimization: Utilizes Random Forest Regressor retrained with selected features for optimal performance.

## Tech Stack

1. Python: The core language used for data processing, model training, and Flask web application development.

2. Flask: A lightweight web framework to serve the predictive model and provide a user-friendly interface.

3. Joblib: For saving and loading the machine learning model and feature sets.

## Machine Learning:

1. Random Forest Regressor: Chosen for its robustness and accuracy in regression tasks.

2. Feature Engineering: Includes selected features such as temperature_fahrenheit, feels_like_celsius, and moonlight_duration for precise predictions

## Dataset

The dataset includes various meteorological parameters, such as:

`temperature_celsius`

`condition_text`

`wind_mph`

`humidity`

`moon_phase`

`daylight_duration`

With over 43 unique weather conditions, the dataset provides a diverse and comprehensive foundation for accurate weather forecasting

## How It Works

1. Data Preprocessing: The dataset undergoes cleaning, feature selection, and transformation to ensure quality input for the model.

2. Model Training: The Random Forest Regressor is trained using selected features, optimized for high accuracy.

3. Web Application: A Flask app provides an intuitive interface for users to input weather features and view predictions.

4. Prediction Display: The app displays both the predicted temperature and the associated weather condition.

   ## Installation and Setup

   `Install dependencies:`
   pip install -r requirements.txt


   `Run the Flask app:`
   python app.py

   ![Weather Prediction](dalleimage.jpg)

   
