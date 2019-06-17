# Model used for prediction
import numpy as np
import pandas as pd

def create_model():
    global train, test, X_test, y_test, model
    # reading dataset
    train = pd.read_csv('final_train.csv')
    test = pd.read_csv('final_test.csv')

    features = train.iloc[:, [2, 3, 4]].values
    label = train.iloc[:, 1].values
    X_test = test.iloc[:, [2, 3, 4]].values
    y_test = test.iloc[:, 1].values

    # Import Gaussian Naive Bayes model
    from sklearn.naive_bayes import GaussianNB

    # Create a Gaussian Classifier
    model = GaussianNB()

    # Train the model using the training sets
    model.fit(features, label)


if __name__ == "__create_model__":
    create_model()


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
    return confusion_matrix


if __name__ == "__confusion_mtarix__":
    confusion_mtarix()
