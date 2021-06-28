from newspaper import Article
import nltk
from gtts import gTTS
import os
a = input("Enter link:")
article = Article(a)
try:
    article.download()
    article.parse()
except newspaper.article.ArticleException:
    print("Not found")
nltk.download('punkt')
article.nlp()
mytext = article.text
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("read_article.mp3")
os.system("start read_article.mp3")
