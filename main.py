# Cleaning the text:
# 1. Create a text file and take text from it (read the text)
import nltk as nltk

text= open('obama.txt',encoding='utf-8').read()
#print(text)

# 2. convert the letter into lowercase
lower_case= text.lower()
#print(lower_case)

# 3. Remove punctuation
import string
#print(string.punctuation)

cleaned_text= lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)

#Tokenization and stop words:
#tokenized_words= cleaned_text.split()
# or you can use the word_tokenizer by nltk
#print(tokenized_words)
#print(len(cleaned_text))
#print(len(tokenized_words))



#import nltk
#nltk.download()


from nltk.corpus import wordnet
from nltk.corpus import stopwords
sw= stopwords.words('english')
#print(sw)

#final_words=[]
#or word in tokenized_words:
 #   if word not in sw:
   #     final_words.append(word)
#print(final_words)
#print(len(final_words))



#5. Algorithem for emotion and text analysis: a list of words with their emotions attitude.
#6. using nltk tokenizer
from nltk.tokenize import word_tokenize
tokenized_words= word_tokenize(cleaned_text, "english")
#print(tokenized_words)
from nltk.corpus import stopwords
sw= stopwords.words('english')
final_words=[]
for word in tokenized_words:
    if word not in sw:
        final_words.append(word)
#print(final_words)
#print(len(final_words))


from nltk.sentiment.vader import SentimentIntensityAnalyzer
def sentiment_analyse(sentiment_text):
    score= SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg= score['neg']
    pos= score['pos']
    if neg> pos:
        print("Negative Sentiment")
    elif pos> neg:
        print("Positive Sentiment")
    else:
        print("Neutral Vibes")
        
    #print(score)
sentiment_analyse(cleaned_text)
