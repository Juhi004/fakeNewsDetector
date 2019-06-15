# for converting the input statement for prediction
import numpy as np
from data_processing import vectorizerTopic, vectorizerSpeaker, vectorizerStatement
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# converting statement
def convert_statement(var):
    filtered_sentence = ""
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(var)
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence = filtered_sentence + " " + w
    vector1 = vectorizerStatement.transform([filtered_sentence])
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
    filtered_sentence = ""
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(var)
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence = filtered_sentence + " " + w
    vector1 = vectorizerTopic.transform([filtered_sentence])
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
    filtered_sentence = ""
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(var)
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence = filtered_sentence + " " + w
    vector1 = vectorizerSpeaker.transform([filtered_sentence])
    arr1 = vector1.toarray()
    tup1 = arr1.shape
    length1 = tup1[1]
    count1 = 0
    for j in range(0, length1):
        if arr1[0, j] != 0:
            count1 = count1 + 1
    sum1 = np.sum(arr1)
    if count1 != 0:
        ans1 = sum1 / count1
    else:
        ans1 = sum1
    return ans1


if __name__ == "__convert_speaker__":
    convert_speaker(var)
