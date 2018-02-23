from PyDictionary import PyDictionary
import numpy as np
from textblob import Word
import nltk

nltk.download('wordnet')

mydict = PyDictionary()

def dict_lookup(arr):
    temp = []
    for entries in arr:
        if len(mydict.synonym(entries)) > 1:
            temp1 = mydict.synonym(entries)
            for item in temp1:
                temp.append(item)
        else:
            temp.append(thisd.synonym(entries))
    newarr = temp + arr
    temp = []
    for entry in newarr:
        t = Word(entry)
        temp.append(t.lemmatize())
        #print(t.lemmatize())
    print(temp)
    print(newarr)
    #newestarr = temp + newarr
    #print(newestarr)
    #return newestarr
    return newarr
