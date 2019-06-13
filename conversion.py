# for converting the input statement for prediction
import data_processing as dp
import numpy as np
from data_processing import vectorizerTopic, vectorizerSpeaker, vectorizerStatement

print("encoding input")

# converting statement
def convert_statement(var):
    var = [var]
    vector1 = vectorizerStatement.transform(var)
    arr1 = vector1.toarray()
    tup1 = arr1.shape
    length1 = tup1[1]
    count1 = 0
    for j in range(0, length1):
        if arr1[0, j] != 0:
            count1 = count1+1
    sum1 = np.sum(arr1)
    if count1 != 0:
        ans1 = sum1/count1
    else:
        ans1 = sum1
    return ans1


if __name__ == "__convert_one__":
    convert_statement(var)


# converting topic
def convert_topic(var):
    var = [var]
    vector1 = vectorizerTopic.transform(var)
    arr1 = vector1.toarray()
    tup1 = arr1.shape
    length1 = tup1[1]
    count1 = 0
    for j in range(0, length1):
        if arr1[0, j] != 0:
            count1 = count1+1
    sum1 = np.sum(arr1)
    if count1 != 0:
        ans1 = sum1/count1
    else:
        ans1 = sum1
    return ans1


if __name__ == "__convert_topic__":
    convert_topic(var)


# converting speaker
def convert_speaker(var):
    var = [var]
    vector1 = vectorizerSpeaker.transform(var)
    arr1 = vector1.toarray()
    tup1 = arr1.shape
    length1 = tup1[1]
    count1 = 0
    for j in range(0, length1):
        if arr1[0, j] != 0:
            count1 = count1+1
    sum1 = np.sum(arr1)
    if count1 != 0:
        ans1 = sum1/count1
    else:
        ans1 = sum1
    return ans1


if __name__ == "__convert_speaker__":
    convert_speaker(var)
