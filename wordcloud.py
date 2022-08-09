import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import WordCloud
import string

nltk.download('punkt')

text = open('/content/drive/MyDrive/Colab Notebooks/img/......', mode = 'r', encoding = 'utf-8').read()
text = text.lower()

sem_pontuacao = ' '.join([p for p in text if p not in string.punctuation])
print(sem_pontuacao)

tokenizar = nltk.word_tokenize(sem_pontuacao)
print(tokenizar)

nltk.download('stopwords')
stopwords = stopwords.words('portuguese')
print(stopwords)

not_stopwords = [p for p in tokenizar if p not in stopwords]
print(stopwords)

not_stopwords = [p for p in tokenizar if p not in stopwords]
print(stopwords)

cloud = WordCloud(
	background_color = 'white',
	stopwords = stopwords,
	height = 1080,
	width = 1080,
	max_words = 100
)

cloud.generate(text)
cloud.to_file('/mycloud.png')
