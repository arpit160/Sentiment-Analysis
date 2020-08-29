import string
from collections import Counter
import GetOldTweets3 as got
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
print('enter')
c=str(input())
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(c).setSince("2020-01-01").setUntil("2020-05-1").\
    setMaxTweets(100)
# get tweets will return a list of tweets recieved by tweetCriteria
tweet_list = got.manager.TweetManager.getTweets(tweetCriteria)

t=""
for tweet in tweet_list:
    t+=tweet.text
    t+=" "
tt=""
s=string.punctuation
# removig punctuations
for i in t:
    if i not in s:
        tt+=i

tt=tt.lower()

#predicting overall sentiment
score=SentimentIntensityAnalyzer().polarity_scores(tt)
if score['pos']>score['neg']:
    print('positive sentiment')
elif score['neg']>score['pos']:
    print('negative sentiment')
else:
    print("neutral sentiment")

#tokenization

token_list=tt.split(' ')

# removig stop words

l=[]
for word in token_list:
    if word not in stopwords.words('english'):
        l.append(word)

#lemmantization

final_list=[]
for word in l:
    w=WordNetLemmatizer().lemmatize(word)
    final_list.append(w)

# emotion list

emotion_list=[]
f=open('emotions.txt','r')
for line in f:
    if ':'in line:
        line=line.replace(',','').replace("'",'').strip()
        word,emotion=line.split(':')
        if word in final_list:
            emotion_list.append(emotion)

d=Counter(emotion_list)
plt.bar(d.keys(),d.values())
plt.xlabel("Emotion")
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
