from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import joblib
from sklearn import tree
# loading data
music_dt  =pd.read_csv('music.csv')

# display the data
print(music_dt.info())

# # prepare 2 groups (features, output)
X=music_dt.drop(columns=['genre']) # sample features (age,gender)
Y=music_dt['genre'] # sample output (genre)

model = DecisionTreeClassifier()
model.fit(X,Y) # load features and sample data
tree.export_graphviz(model,out_file='music_rec.dot',feature_names=['age','gender'],class_names=sorted(Y.unique()),label='all',rounded=True,filled=True)

predictions= model.predict([[15,1],[60,0]]) # make prediction base on the features and samp output
print(predictions)

joblib.dump(model, 'our_pridction.joblib') #binary file