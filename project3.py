import nltk
nltk.download()
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


message = input("What would you like to check?")
lemmed = [WordNetLemmatizer().lemmatize(w) for w in words] #takes all words from the dictionary
wrong_words = set(stopwords.words("english"))

for word in message:
    if word.casefold() not in lemmed: #
        message.append(word) #Store all words that are spelt wrong
print (message) #Print out words that are spelt wrong and not in the dictionary

