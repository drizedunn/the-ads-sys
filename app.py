import numpy as np
from flask import Flask, request, jsonify, render_template, Request
from joblib import load
import sklearn

# Create flask app
flask_app = Flask(__name__)
model = load("model.joblib")

@flask_app.route("/")
def index():
    return render_template("index.html")

@flask_app.route("/form")
def form():
    return render_template("forms.html")

@flask_app.route("/your_ads", methods = ["POST"])
def your_ads():
    user_id = request.form.get('user_id')
    category = request.form.get('category')
    price = request.form.get('price')
    event_type = request.form.get('event_type')
    activity_count = request.form.get('activity_count')
    day = request.form.get('day')
    income = request.form.get('income')
    age = request.form.get('age')
    marriage_status = request.form.get('marriage_status')
    profession = request.form.get('profession')
    country = request.form.get('country')

    pred = model.predict([[event_type, price, user_id, category, activity_count, income, age, marriage_status, profession, country, day]])

    if pred[0] == 3:
        return render_template('acer.html')
    elif pred[0] == 0:
        return render_template('samsung.html')
    elif pred[0] == 2:
        return render_template('huawei.html')
    elif pred[0] == 1:
        return render_template('xiaomi.html')
    elif pred[0] == 4:
        return render_template('apple.html')
    else:
        return render_template('others.html')


if __name__ == "__main__":
    flask_app.run(debug=True)