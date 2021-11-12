import nltk
import json
import random
from nltk.sem.logic import typecheck

intents = json.loads(open('intents.json', encoding='utf-8').read())
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

words=[]
classes = []
documents = []

def main():
    getTag()

def getTag():
    for intent in intents['intents']:
        for pattern in intent['patterns']:
    
            #tokenize each word
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            #add documents in the corpus
            documents.append((w, intent['tag']))
    
            # add to our classes list
            if intent['tag'] not in classes:
                classes.append(intent['tag'])

def getWord(intent):
    word = []
    for pattern in intent['patterns']:

        w = nltk.word_tokenize(pattern)
        word.extend(w)
        #add documents in the corpus
        documents.append((w, intent['tag']))

        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
    return word

typeC = ''
def getResponse(text): 
    for intent in intents['intents']:
        if intent['tag'] == typeC:
            result = random.choice(intent['responses'])
            return str(result)


def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words
    

def bow(sentence):
    # tokenize the pattern
    max = 0
    global typeC
    for intent in intents['intents']:

        sentence_words = clean_up_sentence(sentence)
        word = getWord(intent)

        bag = [0]*len(word) 
        index = 0
        temp = 0
        for s in sentence_words:
            index += 1
            for i,w in enumerate(word):
                if w == s: 
                    # assign 1 if current word is in the vocabulary position
                    bag[i] = 1
                    temp += 1
            # if index == len(words):
            #     break
        if temp >= max and temp != 0:
            type = intent
            typeC = intent['tag']
            max = temp

    try:
        if type:
            return True
    except:
        return False

