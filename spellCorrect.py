
# coding: utf-8

# In[2]:


from flask import Flask
import re
from nltk.tokenize import word_tokenize
# import nltk
# nltk.download('popular')
from spellchecker import SpellChecker
sc = SpellChecker()

app = Flask(__name__)

@app.route("/spellCorrect/<text>")
def spellCorrect(text):
    # saving original word for later reference
    # text_o = text
    # print(text_o)
    text = str(text)
    
    # cleaning the input text
    text = text.strip() 
    text = text.lower()
    text = re.sub('-', ' ', text)
    text = re.sub('[^A-Za-z ]+', '', text)
    # print(text)
    
    # getting words from the text
    tokens = word_tokenize(text)
    # print(tokens)
    
    # checking lengh of text and number of words
    l = len(text)
    # print(l)
    n = len(tokens)
    # print(n)
    
    # setting up distance criterion based on length of text
    if(l<=8):
        sc.distance = 2
    else:
        sc.distance = 1
    
    # suggesting corrections
    if(n<1):
        return "Love HaikuJAM"
    
    if(n==1):
        t = tokens[0]
        c1 = sc.candidates(t)
        c1 = [sc.known([w]) for w in c1]
        c1 = [w for s in c1 for w in s]
        if(len(c1)>3):
            c1 = c1[0:3]
        
        c2 = []
        if(l>3):
            splits = [[t[:i], t[i:]] for i in range(2,(l-1))]
            for ww in splits:
                c = [sc.correction(w) for w in ww]
                c = list([sc.known([w]) for w in c])
                c = ' '.join(w for s in c for w in s)
                c2.append(c)
        
        corrections = list(set(c1)) + list(set(c2))
        corrections = ', '.join(w for w in corrections)
        return corrections
    
    if(n>1):
        c = [sc.correction(t) for t in tokens]
        c = list([sc.known([w]) for w in c])
        c = ' '.join(w for s in c for w in s)
        corrections = list(set([c]))
        corrections = ', '.join(w for w in corrections)
        return corrections

if __name__ == '__main__':
    app.run()
    
# Further improvements:
# The ideal way would be to check the words against a dictionary that has been built specifially for the HaikuJAM app.
# This threshold(=10) on lenght of text could be decided depending on the desired response time.
# Order of suggestions could be decided on latent probabilities.


# In[312]:


from flask import Flask
import re
from nltk.tokenize import word_tokenize
# import nltk
# nltk.download('popular')
from spellchecker import SpellChecker
sc = SpellChecker()

app = Flask(__name__)

@app.route("/spellCorrect/<text>")
def spellCorrect(text):
    return text
    
if __name__ == '__main__':
    app.run()
    
# Further improvements:
# The ideal way would be to check the words against a dictionary that has been built specifially for the HaikuJAM app.
# This threshold(=10) on lenght of text could be decided depending on the desired response time.
# Order of suggestions could be decided on latent probabilities.


# In[318]:


def spellCorrect(text):
    # saving original word for later reference
    # text_o = text
    # print(text_o)
    text = str(text)
    
    # cleaning the input text
    text = text.strip() 
    text = text.lower()
    text = re.sub('-', ' ', text)
    text = re.sub('[^A-Za-z ]+', '', text)
    # print(text)
    
    # getting words from the text
    tokens = word_tokenize(text)
    # print(tokens)
    
    # checking lengh of text and number of words
    l = len(text)
    # print(l)
    n = len(tokens)
    # print(n)
    
    # setting up distance criterion based on length of text
    if(l<=8):
        sc.distance = 2
    else:
        sc.distance = 1
    
    # suggesting corrections
    if(n<1):
        return "Love HaikuJAM"
    
    if(n==1):
        t = tokens[0]
        c1 = sc.candidates(t)
        c1 = [sc.known([w]) for w in c1]
        c1 = [w for s in c1 for w in s]
        if(len(c1)>3):
            c1 = c1[0:3]
        
        c2 = []
        if(l>3):
            splits = [[t[:i], t[i:]] for i in range(2,(l-1))]
            for ww in splits:
                c = [sc.correction(w) for w in ww]
                c = list([sc.known([w]) for w in c])
                c = ' '.join(w for s in c for w in s)
                c2.append(c)
        
        corrections = list(set(c1)) + list(set(c2))
        corrections = ', '.join(w for w in corrections)
        return corrections
    
    if(n>1):
        c = [sc.correction(t) for t in tokens]
        c = list([sc.known([w]) for w in c])
        c = ' '.join(w for s in c for w in s)
        corrections = list(set([c]))
        corrections = ', '.join(w for w in corrections)
        return corrections

spellCorrect("HiBro")

