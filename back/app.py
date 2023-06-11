from flask import Flask, request
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from flask_cors import CORS
import csv
import joblib


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/pred', methods=['POST'])
def pred():
    # read my DB (CSV)
    # music_dt = pd.read_csv('music.csv')

    # # prepare 2 groups (features, output)
    # X = music_dt.drop(columns=['genre'])  # sample features (age,gender)
    # Y = music_dt['genre']  # sample output (genre)

    # print(music_dt.info())
    # model = DecisionTreeClassifier()
    # model.fit(X, Y)  # load features and sample data

    # get data from the user
    data = request.json
    age = data.get('age')
    gender = data.get('gender')
    
    model=joblib.load('our_pridction.joblib')
    predictions= model.predict([[age,gender]])
    # make prediction base on the features and samp output
    return {'pred': predictions[0]}


@app.route('/learn', methods=['POST'])
def learn():
    # get data from the user
    data = request.json
    age = data.get('age')
    gender = data.get('gender')
    genre = data.get('genre')
    
    """
    write new row to CSV
    """
    with open('music.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([age,gender,genre])
    music_dt = pd.read_csv('music.csv')

    # # prepare 2 groups (features, output)
    X = music_dt.drop(columns=['genre'])  # sample features (age,gender)
    Y = music_dt['genre']  # sample output (genre)
    model = DecisionTreeClassifier()
    model.fit(X, Y)  # load features and sample data
    joblib.dump(model, 'our_pridction.joblib') #binary file
    return {"learn":True}


if __name__ == '__main__':
    app.run(debug=True)
