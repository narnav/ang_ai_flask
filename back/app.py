from flask import Flask, request
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/pred', methods=['POST'])
def pred():
    # read my DB (CSV)
    music_dt = pd.read_csv('music.csv')

    # # prepare 2 groups (features, output)
    X = music_dt.drop(columns=['genre'])  # sample features (age,gender)
    Y = music_dt['genre']  # sample output (genre)

    # print(music_dt.info())
    model = DecisionTreeClassifier()
    model.fit(X, Y)  # load features and sample data

    # get data from the user
    data = request.json
    age = data.get('age')
    gender = data.get('gender')

    # make prediction base on the features and samp output
    predictions = model.predict([[age, gender]])
    return {'pred': predictions[0]}


if __name__ == '__main__':
    app.run(debug=True)
