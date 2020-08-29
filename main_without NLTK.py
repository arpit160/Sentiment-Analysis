import string
from collections import Counter
import matplotlib.pyplot as plt

f=open('content.txt',encoding='utf-8')      #by default file will open in read mode.
t=''
for line in f:
    if line!='\n':
        line=line.strip()
        t+=line
        t+=' '
t=t.lower()
s=string.punctuation     #returns a constant string

l=""
for i in t:
    if i not in s:
        l+=i
ll=l.split(' ')
print(ll)
stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#removing stop words
final=[]
for i in ll:
    if i not in stop_words:
        final.append(i)

emotion_list=[]
g=open('emotions.txt','r')

for i in g:
    if ':' not in i:
        continue
    else:
        i=i.replace("'","").replace(',','').replace('\n',' ').strip()
        word,emotion=i.split(":")
        if word in final:
            emotion_list.append(emotion)

print(emotion_list)

d=Counter(emotion_list)
x=[]
y=[]
for i in d:
    x.append(i)
    y.append(d[i])

plt.bar(x,y)
plt.xlabel("emotion")
plt.ylabel('frequency')
plt.xticks(rotation=45)
plt.show()


