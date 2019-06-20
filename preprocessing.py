import xlrd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

vectorizerStatement = TfidfVectorizer()
vectorizerTopic = TfidfVectorizer()
vectorizerSpeaker = TfidfVectorizer()

wb11 = xlrd.open_workbook("train.xlsx")
wb21 = xlrd.open_workbook("test.xlsx")
train_dataset = wb11.sheet_by_index(0)
test_dataset = wb21.sheet_by_index(0)

stop_words = set(stopwords.words('english'))

text1 = []
text2 = []
text3 = []

n = train_dataset.nrows

filtered_sentence = ""

for i in range(1, n):
    word_tokens = word_tokenize(train_dataset.cell_value(i, 1))
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence = filtered_sentence + " " + w
    text1.append(filtered_sentence)

    filtered_sentence = ""
    word_tokens = word_tokenize(train_dataset.cell_value(i, 2))
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence = filtered_sentence + " " + w
    text2.append(filtered_sentence)

    filtered_sentence = ""
    word_tokens = word_tokenize(train_dataset.cell_value(i, 3))
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence = filtered_sentence + " " + w
    text3.append(filtered_sentence)

vectorizerStatement.fit(text1)
vectorizerTopic.fit(text2)
vectorizerSpeaker.fit(text3)
