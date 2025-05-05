from flask import Flask, request, render_template
import pickle

# Create the app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get all four input values
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Make a prediction
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        # Show the prediction on the webpage
        return render_template('index.html', prediction_text=f'Predicted Class: {prediction[0]}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


