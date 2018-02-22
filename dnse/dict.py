from PyDictionary import PyDictionary
import numpy as np

thisd = PyDictionary()

def dict_lookup(arr):
    temp = []
    for entries in arr:
        if len(thisd.synonym(entries)) > 1:
            temp1 = thisd.synonym(entries)
            for item in temp1:
                temp.append(item)
        else:
            temp.append(thisd.synonym(entries))
    newarr = temp + arr
    #print(newarr)
    return newarr
