from flask import Flask, render_template, request, flash
import pandas as pd
import pickle
import numpy as np
from datetime import datetime
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Load the model
try:
    with open('model.pkl', 'rb') as file:
        saved_model = pickle.load(file)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    saved_model = None


def validate_input(data):
    """Validate user input data"""
    errors = []

    # Check if all fields are filled
    if not all(data.values()):
        errors.append("All fields must be filled")
        return False, errors

    try:
        # Convert and validate numeric fields
        duration = float(data['duration'])
        days_left = int(data['days_left'])

        if duration <= 0 or duration > 24:
            errors.append("Duration must be between 0 and 24 hours")

        if days_left < 0 or days_left > 365:
            errors.append("Days left must be between 0 and 365")

    except ValueError:
        errors.append("Invalid numeric values for duration or days left")
        return False, errors

    # Validate categorical fields
    valid_airlines = {'SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India'}
    valid_cities = {'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'}
    valid_times = {'Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night'}
    valid_categories = {'Business', 'Economy'}

    if data['airline'] not in valid_airlines:
        errors.append("Invalid airline selected")
    if data['source_city'] not in valid_cities:
        errors.append("Invalid source city selected")
    if data['destination_city'] not in valid_cities:
        errors.append("Invalid destination city selected")
    if data['departure_time'] not in valid_times:
        errors.append("Invalid departure time selected")
    if data['arrival_time'] not in valid_times:
        errors.append("Invalid arrival time selected")
    if data['category'] not in valid_categories:
        errors.append("Invalid category selected")

    # Check if source and destination are different
    if data['source_city'] == data['destination_city']:
        errors.append("Source and destination cities cannot be the same")

    return len(errors) == 0, errors


def format_price(price):
    """Format the predicted price with proper currency symbol and formatting"""
    try:
        return f"₹{price:,.2f}"
    except:
        return str(price)


@app.route('/')
@app.route('/home')
def home():
    return render_template("predict.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if saved_model is None:
            logger.error("Model not loaded")
            return render_template('predict.html',
                                   pred="Error: Service temporarily unavailable. Please try again later.")

        # Get form data
        input_data = {
            'airline': request.form.get('airline'),
            'source_city': request.form.get('source_city'),
            'departure_time': request.form.get('departure_time'),
            'arrival_time': request.form.get('arrival_time'),
            'destination_city': request.form.get('destination_city'),
            'category': request.form.get('category'),
            'duration': request.form.get('duration'),
            'days_left': request.form.get('days_left')
        }

        # Validate input
        is_valid, errors = validate_input(input_data)
        if not is_valid:
            error_message = " | ".join(errors)
            logger.warning(f"Input validation failed: {error_message}")
            return render_template('predict.html', pred=f"Error: {error_message}")

        # Convert numeric fields
        input_data['duration'] = float(input_data['duration'])
        input_data['days_left'] = int(input_data['days_left'])

        # Create DataFrame for prediction
        x_new = pd.DataFrame([input_data])

        # Make prediction
        prediction = saved_model.predict(x_new)[0]

        # Format message
        formatted_price = format_price(prediction)
        message = f"Predicted Price: {formatted_price}"

        logger.info(
            f"Successful prediction made for flight from {input_data['source_city']} to {input_data['destination_city']}")

        return render_template('predict.html', pred=message)

    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return render_template('predict.html',
                               pred="An unexpected error occurred. Please try again later.")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('predict.html', pred="Page not found"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('predict.html', pred="Internal server error. Please try again later."), 500


if __name__ == '__main__':
    app.run(debug=True)