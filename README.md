# ✈️ Flight Price Prediction System with Machine Learning

[![Application Status](https://img.shields.io/website?url=https%3A%2F%2Fflight-price-predictor-m5k2.onrender.com%2F)](https://flight-price-predictor-m5k2.onrender.com/)

This project is a web-based application designed to predict flight prices based on user-provided travel details. By utilizing a machine learning model trained on historical flight data, this system empowers users to make cost-effective booking decisions by providing estimated prices for flights.

🌐 **Project Link**: [Flight Price Predictor](https://flight-price-predictor-m5k2.onrender.com/)

---

## 🛠️ System Architecture

The system architecture is divided into two main components: the **Machine Learning Model** and the **Web Application**.

### 1. 🧠 Machine Learning Model

The core of the prediction system is a machine learning model that estimates flight prices based on various travel-related factors.

- **Data Collection**: 
  - 📊 Data from Kaggle, including attributes like:
    - Source and Destination Cities
    - Airline
    - Duration
    - Number of Stops
    - Ticket Price
- **Data Preprocessing**: 
  - 🧹 The data undergoes cleaning and preprocessing:
    - Handling missing values
    - Encoding categorical variables
    - Scaling features to improve model performance
- **Model Training**: 
  - 🌲 **Random Forest Regression** model is trained on the dataset to accurately predict flight prices.
- **Model Evaluation**:
  - 🧮 Metrics such as **Mean Squared Error (MSE)** and **R-Squared** are used to evaluate accuracy and performance.

### 2. 🌐 Web Application

The user-facing application is built with the **Flask** framework, making it easy for users to interact with the model.

- **Flask Framework**: Provides a lightweight backend.
- **User Interface (UI)**:
  - ✍️ Users can input:
    - Source City, Destination City
    - Travel Date, Preferred Airline (optional)
    - Number of Stops (optional)
- **API Integration**:
  - 🔗 The Flask API connects the frontend with the trained model for real-time predictions.
- **Price Prediction and Display**:
  - 💵 The API returns a predicted price based on input details, displayed alongside a disclaimer.

---

## 📝 Implementation Steps

1. **Data Acquisition**:
   - 📥 Gather historical flight data from Kaggle.

2. **Data Preprocessing**:
   - 🧹 Clean and transform data, encode categorical variables, and scale numerical features.

3. **Model Development**:
   - 🤖 Train a **Random Forest Regression** model on the dataset.

4. **Model Evaluation**:
   - 🧮 Evaluate the model using MSE and R-Squared metrics.

5. **API Development**:
   - 🔗 Build a Flask API to serve model predictions to the web app.

6. **Web Application Development**:
   - 🖥️ Create a user-friendly UI with Flask for interaction.

7. **Deployment**:
   - 🚀 Deploy on a hosting platform (e.g., Render).

---

## 🌟 Benefits

- **Cost Savings** 💰: Allows users to make strategic booking choices.
- **Informed Decisions** 🧭: Offers users a chance to compare options and book cost-effectively.
- **Travel Planning Optimization** 📅: Supports users with budget references for better planning.

---

## 🔧 Tools and Technologies

- **Programming Language**: Python 🐍
- **Machine Learning Library**: Scikit-learn 🤖
- **Web Framework**: Flask 🌐
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib 📊, Seaborn 📉
- **Deployment**: Render 🛠️
