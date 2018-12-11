import json
import nltk
import numpy as np
import scipy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import OrderedDict
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()
tfidf_vectorizer = TfidfVectorizer()


# read FAQ question and answer
df = pd.read_csv('data/Q_and_A.csv')
questions = df['question'].tolist()
answers = df['answer'].tolist()


#read test.txt
test_sentences = open('data/test.txt', 'r').read().strip().split('\n')




def lemmatize_words(sent):
    return ' '.join([lemmatizer.lemmatize(word) for word in sent.split()])

lemmatized_questions = [lemmatize_words(question) for question in questions]


tfidf_vectorizer.fit(lemmatized_questions)


class Chatbot:
    def __init__(self):
        self.q_tfidf = tfidf_vectorizer.transform(lemmatized_questions)

    def get_answer(self, question):
        lemmatized_question = lemmatize_words(question)
        vectorized_sentence = tfidf_vectorizer.transform([lemmatized_question])
        ans_idx = np.argmax(cosine_similarity(self.q_tfidf, vectorized_sentence))
        predicted_ans = answers[ans_idx]
        return predicted_ans


if __name__ == "__main__":

    # created an instance of Chatbot class
    chatbot = Chatbot()

    # loop through each test sentence, get relevant answer and create a csv in same folder
    test_q_a_list = []
    for test_question in test_sentences:
        test_dict = {}

        answer = chatbot.get_answer(test_question)

        test_dict['question'] = test_question
        test_dict['answers'] = answer
        test_q_a_list.append(test_dict)

    df = pd.DataFrame(test_q_a_list)
    df.to_csv('data/test_Q_and_A.csv')





