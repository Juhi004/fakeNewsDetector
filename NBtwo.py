import numpy as np
import pandas as pd

print("stating NBtwo")

# reading dataset
train = pd.read_csv('new_train.csv')
test = pd.read_csv('new_test.csv')

features = train.iloc[:, [1, 2, 3]].values
label = train.iloc[:, 0].values
X_test = test.iloc[:, [1, 2, 3]].values
y_test = test.iloc[:, 0].values

print("Files have been read")


#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(features, label)

print("model has been created and features ahve been fitted")

"""

# print(train.head(10))
# train.describe()

# print(test.head(10))
# test.describe()

# Import LabelEncoder
from sklearn import preprocessing
# creating labelEncoder
le = preprocessing.LabelEncoder()
print("three")
# Converting string labels into numbers.
weather_encoded=le.fit_transform(weather)
print(weather_encoded)

# Converting string labels into numbers
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print("Temp:",temp_encoded)
print("Play:",label)


#Combinig weather and temp into single listof tuples
features = zip(weather_encoded,temp_encoded)
print(features)
featuresA = np.array(features).reshape(1,-1)
print(featuresA)
"""


def predict(v1, v2, v3):
    predicted = model.predict([[v1, v2, v3]])
    print("Predicted Value:", predicted)
    return predicted


if __name__ == "__predict__":
    predict(a, b, c)


# confusion matrix
def confusion_mtarix():
    # Predict Output
    y_pred = model.predict(X_test)
    tp=len([i for i in range(0,y_test.shape[0]) if y_test[i]==0 and y_pred[i]==0])
    tn=len([i for i in range(0,y_test.shape[0]) if y_test[i]==0 and y_pred[i]==1])
    fp=len([i for i in range(0,y_test.shape[0]) if y_test[i]==1 and y_pred[i]==0])
    fn=len([i for i in range(0,y_test.shape[0]) if y_test[i]==1 and y_pred[i]==1])
    confusion_matrix = np.array([[tp, tn],[fp, fn]])
    print("Confusion matrix-")
    print(confusion_matrix)


if __name__ == "__confusion_mtarix__":
    confusion_mtarix()

