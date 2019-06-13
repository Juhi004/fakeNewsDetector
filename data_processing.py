# Creating vocabulary and saving TF-IDF for each entry in the training and testing dataset
# into new files which will be used for further processing
import xlrd
import openpyxl
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.stats import pearsonr
from matplotlib import pyplot

# Give the location of the file
data_folder = Path("C:/Users/DELL/PycharmProjects/TrialAndTest/")
loc1 = data_folder / "train.xlsx"
loc2 = data_folder / "test.xlsx"
# To open Workbook
wb11 = xlrd.open_workbook(loc1)
wb21 = xlrd.open_workbook(loc2)
train_dataset = wb11.sheet_by_index(0)
test_dataset = wb21.sheet_by_index(0)

# loc1 = data_folder / "new_train.xlsx"
loc2 = data_folder / "new_test.xlsx"
# To open Workbook
# workbook1 = openpyxl.load_workbook('new_train.xlsx')
# workbook2 = openpyxl.load_workbook('new_test.xlsx')
# train = workbook1.worksheets[0]
# test = workbook2.worksheets[0]

text1 = []
text2 = []
text3 = []
statement = []
topics = []
speaker = []
print(train_dataset.nrows)
print("///////")
print(test_dataset.nrows)


# converting training data set
n = train_dataset.nrows
#print(n)
for i in range(1, n):
    text1.append(train_dataset.cell_value(i, 1))
    text2.append(train_dataset.cell_value(i, 2))
    text3.append(train_dataset.cell_value(i, 3))
vectorizerStatement = TfidfVectorizer()
vectorizerStatement.fit(text1)
vectorizerTopic = TfidfVectorizer()
vectorizerTopic.fit(text2)
vectorizerSpeaker = TfidfVectorizer()
vectorizerSpeaker.fit(text2)

print("Vectorizers created")

# print("Vocabulary is-")
# print(vectorizerTopic.vocabulary_)
# print("tfid are-")
# print(vectorizerTopic.idf_)

# Converting the training and testing data into numeric form for processing
"""
for i in range(0, n):
    vector1 = vectorizerStatement.transform([train_dataset.cell_value(i, 3)])
    vector2 = vectorizerTopic.transform([train_dataset.cell_value(i, 6)])

    arr1 = vector1.toarray()
    arr2 = vector2.toarray()

    tup1 = arr1.shape
    tup2 = arr2.shape
    length1 = tup1[1]
    length2 = tup2[1]
    count1 = 0
    count2 = 0

    for j in range(0, length1):
        if arr1[0, j] != 0:
            count1 = count1+1
    for j in range(0, length2):
        if arr2[0, j] != 0:
            count2 = count2 + 1

    sum1 = np.sum(arr1)
    sum2 = np.sum(arr2)

    if count1 != 0:
        ans1 = sum1/count1
    else:
        ans1 = sum1
    if count2 != 0:
        ans2 = sum2/count2
    else:
        ans2 = sum2

    statement.append(ans1)
    topics.append(ans2)
    #verdict.append(train_dataset.cell_value(i, 0))


for i in range(1, n):
    j = train.cell(row=i, column=1)
    j.value = verdict[i]
workbook1.save('new_train.xlsx')

for i in range(1, n):
    j = train.cell(row=i, column=4)
    j.value = statement[i]
workbook1.save('new_train.xlsx')

for i in range(1, n):
    j = train.cell(row=i, column=5)
    j.value = topics[i]
workbook1.save('new_train.xlsx')


# converting testing data set
text1 = []
text2 = []
statement = []
topics = []
verdict = []
n = test_dataset.nrows
#print(n)
for i in range(1, n):
    text1.append(test_dataset.cell_value(i, 3))
    text2.append(test_dataset.cell_value(i, 6))
vectorizerStatement = TfidfVectorizer()
vectorizerStatement.fit(text1)
vectorizerTopic = TfidfVectorizer()
vectorizerTopic.fit(text2)
#print("Vocabulary is-")
# print(vectorizerTopic.vocabulary_)
#print("tfid are-")
# print(vectorizerTopic.idf_)


for i in range(0, n):
    vector1 = vectorizerStatement.transform([test_dataset.cell_value(i, 3)])
    vector2 = vectorizerTopic.transform([test_dataset.cell_value(i, 6)])

    arr1 = vector1.toarray()
    arr2 = vector2.toarray()

    tup1 = arr1.shape
    tup2 = arr2.shape
    length1 = tup1[1]
    length2 = tup2[1]
    count1 = 0
    count2 = 0

    for j in range(0, length1):
        if arr1[0, j] != 0:
            count1 = count1+1
    for j in range(0, length2):
        if arr2[0, j] != 0:
            count2 = count2 + 1

    sum1 = np.sum(arr1)
    sum2 = np.sum(arr2)

    if count1 != 0:
        ans1 = sum1/count1
    else:
        ans1 = sum1
    if count2 != 0:
        ans2 = sum2/count2
    else:
        ans2 = sum2

    statement.append(ans1)
    topics.append(ans2)
    #verdict.append(test_dataset.cell_value(i, 0))

for i in range(1, n):
    j = test.cell(row=i, column=1)
    j.value = verdict[i]
workbook2.save('new_test.xlsx')

for i in range(1, n):
    j = test.cell(row=i, column=4)
    j.value = statement[i]
workbook2.save('new_test.xlsx')

for i in range(1, n):
    j = test.cell(row=i, column=5)
    j.value = topics[i]
workbook2.save('new_test.xlsx')

print('finish')

#np.seterr(divide='ignore', invalid='ignore')
#covariance = np.cov(topics, verdict)
#print(covariance)
#corr, _ = pearsonr(topics, verdict)
#Eprint('Pearsons correlation: %.3f' % corr)
#pyplot.scatter(topics, verdict)
#pyplot.show()
#print(topics)
#print(corr, _)
"""


def get_vocab_statement():
    return vectorizerStatement


if __name__ == "__get_vocab_statement__":
    get_vocab_statement()


def get_vocab_one(data):
    n = data.nrows
    for j in range(1, n):
        text1.append(data.cell_value(j, 2))
    vectorizerTopic = TfidfVectorizer()
    vectorizerTopic.fit(text1)
    return vectorizerTopic


if __name__ == "__get_vocab_one__":
    get_vocab_one()
