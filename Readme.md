

Which algorithm did you use to match free text with questions in the repository? What were the reasons to select the algorithm?
1. lemmatization of corpus
2. Tf-idf is calculated
3. Cosine similarity is calculated between input question and all questions in corpus
4. Answer for corresponding Question with highest similarity is the returned

Reason for selecting above method are 
1. powerful algorithm 
2. Fast development 
3. decent accuracy


How would you measure accuracy?
1. precision, recall and F1 score is used to measure accuracy whether the algorithm predicted to answer correct or not


How would you improve accuracy?

1. using tf-idf with weighted word2vec
2. pre-processing and taking WH-Questions(what, how , when, etc) into consideration
3. Mapping problem into machine learning problem such as Quora (Quora checks for similar question using Randomforest algorithm) https://engineering.quora.com/Semantic-Question-Matching-with-Deep-Learning
4. Introducing sematic similarity and synonyms
5. Algorithms and techniques such as word mover's distance can be used. http://proceedings.mlr.press/v37/kusnerb15.pdf
6. fuzzy search and spell checker will act as preprocessing to improve question quality 



How would you deal with multiple users speaking with the same bot?

1. Multiple user's will have multiple sessions to talk to same bot
2. Asynchronosity will help with seamless service to users


python scrape_faq.py will scrape all the questions and answers into csv in ./data folder


Go to python terminal and follow below code:

>>> from chatbot import Chatbot
>>> faq = Chatbot()
>>> faq.get_answer('How will my application be evaluated?')


