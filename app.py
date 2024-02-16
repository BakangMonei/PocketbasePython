from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Endpoint for Pocketbase
POCKETBASE_URL = "http://127.0.0.1:8090/api/collections/MelissaDatabase/records"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "firstname": request.form['firstname'],
        "lastname": request.form['lastname'],
        "phonenumber": request.form['phonenumber'],
        "email": request.form['email'],
        "sport": request.form['sport']
    }
    response = requests.post(POCKETBASE_URL, json=data)
    return response.text

@app.route('/get')
def get_data():
    response = requests.get(POCKETBASE_URL)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
