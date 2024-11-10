from flask import Flask, render_template, request
import random
import datetime as dt
import requests

app=Flask(__name__)
AGIFY_URL= "https://agify.io/"
GENDERIZE_URL="https://genderize.io"
@app.route('/')
def home():
    random_number= random.randint(0,10)
    current_year= dt.datetime.now().year
    return render_template('index.html',num=random_number,year=current_year)

@app.route('/guess/<name>')
def details(name):
    age_response= requests.get(f"https://api.genderize.io?name=peter")
    print(age_response.json())
if __name__=="__main__":
    app.run(debug=True)