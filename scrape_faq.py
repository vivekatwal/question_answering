import requests
from lxml import html
import pandas as pd

url = 'https://www.hbs.edu/mba/find-answers/Pages/default.aspx'

res = requests.get(url)
text = html.fromstring(res.content)

faq_sections = text.xpath("//div[@class='ms-rtestate-field']//div[@class='faq-section']")

questions = []
answers = []
for faq_section in faq_sections:

    for q in faq_section.xpath('.//dl//dt'):
        question = q.xpath('.//text()')
        question = ' '.join(question)
        questions.append(question)

    for a in faq_section.xpath('.//dl//dd'):
        answer = a.xpath('.//text()')
        answer = ' '.join(answer)
        answers.append(answer)

df = pd.DataFrame({'question': questions, 'answer': answers})

df.to_csv('data/Q_and_A.csv')

df.head()