# -*- coding: utf-8 -*-
import pickle


class Twin:
    verdict = False
    prob = 0


# doc_new = ['obama is running for president in 2016']

#var = input("Please enter the news text you want to verify: ")
#print("You entered: " + str(var))


# function to run for prediction
def detecting_fake_news(var):
    # retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    p1 = Twin()
    p1.verdict = prediction[0]
    p1.prob = prob[0][1]
    print("Probability: ",prediction[0])
    print("Truth probability score: ", prob[0][1])
    return p1


if __name__ == "__detecting_fake_news__":
    detecting_fake_news(var)



'''
p1 = Twin()
    p1.verdict = prediction[0]
    p1.prob  = prob[0][1]
    print("The given statement is ",prediction[0])
    print("The truth probability score is ",prob[0][1])
    return p1
'''


if __name__ == '__main__':
    detecting_fake_news(var)
