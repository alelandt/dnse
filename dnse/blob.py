from wordsegment import load, segment
import itertools

def check_data(alist):
    for x in alist:
        y = x
        y.append('.')
        print(y)

    return False  

def strip_space(name):
    cleared = str.replace(name, " ", "")
    return cleared

def strip_out(name):
    cleared = str.replace(name, "*", "")
    cleared = str.replace(cleared, " ", "")
    cleared = str.replace(cleared, "-", "")
    cleared = str.replace(cleared, ".", "")
    cleared = str.replace(cleared, ",", "")
    return cleared

def combine_all(locations, syn, tldd):
    garbage = list(map(''.join, itertools.chain(itertools.product(locations, syn), itertools.product(syn, locations))))
    garbage += list(map(''.join, itertools.chain(itertools.product(syn, syn))))
    garbage += syn;
    topGarbage = list(map('.'.join, itertools.chain(itertools.product(garbage,tldd))))

    return topGarbage
    
