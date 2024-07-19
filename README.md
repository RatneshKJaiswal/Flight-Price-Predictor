# Project: Flight Price Prediction System with Machine Learning

This project aims to develop a web application that leverages machine learning to predict flight prices. Users can input their desired travel details and receive an estimated cost for their trip, enabling informed decision-making when booking flights.
Project Link : https://flight-price-predictor-m5k2.onrender.com/

# System Architecture

The system will consist of two main components:

* Machine Learning Model:

  * Data Collection: Historical flight data will be collected from Kaggle's Public Datasets. This data will include attributes like source city, destination city, airline, duration, number of stops, and price.
  * Data Preprocessing: The collected data will be cleaned and preprocessed. This may involve handling missing values, converting categorical variables to numerical representations, and feature scaling.
  * Model Training: A Random Forest algorithm will be trained on the preprocessed data. Random Forest is a robust regression technique suitable for capturing complex relationships within the data. The model will learn to map the input features (source, destination, etc.) to the target variable (flight price).
  * Model Evaluation: The trained model's performance will be evaluated using metrics like mean squared error (MSE) or R-squared. This ensures the model's accuracy in predicting flight prices.

* Web Application:

  * Flask Framework: The web application will be developed using the Flask framework in Python. Flask provides a lightweight and flexible foundation for building user interfaces.
  * User Interface (UI): The UI will allow users to enter their travel details, such as source city, destination city, travel date, preferred airline (optional), and desired number of stops (optional).
  * API Integration: The UI will integrate with the trained machine learning model through an API. When a user submits their travel details, the information will be sent to the API.
  * Price Prediction: The API will receive the user input, process it according to the model's requirements, and generate a predicted flight price using the trained Random Forest model.
  * Price Display: The predicted flight price will be displayed back on the user interface, along with relevant disclaimers about the prediction's nature (estimation).

# Implementation Steps

  * Data Acquisition: Gather historical flight data from Kaggle.
  * Data Preprocessing: Clean and prepare the data for model training.
  * Model Development: Train a Random Forest regression model on the preprocessed data.
  * Model Evaluation: Evaluate the model's performance using appropriate metrics.
  * API Development: Develop a Flask API to expose the trained model for price predictions.
  * Web Application Development: Build a user-friendly web interface using Flask to interact with the API.
  * Deployment: Deploy the web application to a suitable hosting platform.

# Benefits
This project offers several advantages:

  * Cost Savings: Users can leverage price predictions to plan their trips more strategically and potentially save money on flights.
  * Informed Decisions: Early insights into flight prices allow users to compare options and book during cost-effective periods.
  * Travel Planning Optimization: The system aids travel planning by providing a reference point for budgeting and decision-making.

# Tools and Technologies
* Programming Language: Python
* Machine Learning Library: scikit-learn
* Web Framework: Flask
* Additional Libraries: Pandas, NumPy, Matplotlib, Seaborn
* Web API : Render

# Conclusion

This machine learning-based flight price prediction system empowers users with valuable information to navigate the dynamic world of flight pricing. By leveraging the power of Random Forest algorithms and a user-friendly web interface, this project can enhance travel planning and potentially lead to cost savings.
