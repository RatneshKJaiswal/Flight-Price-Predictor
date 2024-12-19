from flask import Flask, render_template, request
import pandas as pd
import pickle

saved_model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


@app.route('/', methods=['GET'])
def home():
    return render_template("predict.html", pred="")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            airline = request.form.get('airline')
            source_city = request.form.get('source_city')
            departure_time = request.form.get('departure_time')
            arrival_time = request.form.get('arrival_time')
            destination_city = request.form.get('destination_city')
            category = request.form.get('category')
            duration = request.form.get('duration')
            days_left = request.form.get('days_left')

            x = {
                'airline': [airline],
                'source_city': [source_city],
                'departure_time': [departure_time],
                'arrival_time': [arrival_time],
                'destination_city': [destination_city],
                'category': [category],
                'duration': [duration],
                'days_left': [days_left]
            }
            x_new = pd.DataFrame(x)
            prediction = saved_model.predict(x_new)[0]
            message = f"Predicted Price : {prediction:,.0f} INR"
            return render_template('predict.html', pred=message)

        except Exception as e:
            return render_template('predict.html', pred="An error occurred during prediction.")

    return render_template('predict.html', pred="")


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('predict.html', pred="Method not allowed"), 405


if __name__ == '__main__':
    app.run(debug=True)