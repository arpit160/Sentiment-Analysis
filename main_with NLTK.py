import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from scipy.spatial.transform import rotation

f = open('content.txt', encoding='utf-8')
t = ''
for line in f:
    if line != '\n':
        t += line
        t += ' '
f.close()
s = string.punctuation
tt = ''
for i in t:
    if i not in s:
        tt += i

tt.lower()

# predicting overall sentiment of text

score=SentimentIntensityAnalyzer().polarity_scores(tt)
if score['pos']>score['neg']:
    print('positive sentiment')
elif score['neg']>score['pos']:
    print('negative sentiment')
else:
    print("neutral sentiment")

# tokenizer is faster than split function
# return a list of words

l = word_tokenize(tt, language="english")
ll = []
for word in l:
    if word not in stopwords.words('english'):
        ll.append(word)

# lemmantizatin

lemma_words = []
for word in ll:
    p = WordNetLemmatizer()
    word = p.lemmatize(word)
    lemma_words.append(word)

f=open('emotions.txt','r')
emotion_list=[]
for line in f:
    if ':' in line:
        line=line.replace(',','').replace("'",'').strip()
        word,emotion=line.split(":")
        if word in lemma_words:
            emotion_list.append(emotion)

f.close()

d=Counter(emotion_list)
x=[]
y=[]
for i in d:
    x.append(i)
    y.append(d[i])

plt.bar(x,y)
plt.xlabel("Emotion")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
plt.savefig('graph.png')