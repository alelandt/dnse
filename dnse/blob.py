from wordsegment import load, segment
import itertools

def strip_out(name):
    cleared = str.replace(name, "*", "")
    cleared = str.replace(cleared, " ", "")
    cleared = str.replace(cleared, "-", "")
    cleared = str.replace(cleared, ".", "")
    cleared = str.replace(cleared, ",", "")
    return cleared

def combine_all(locations, syn, tldd):
    garbage = list(map(''.join, itertools.chain(itertools.product(locations, syn), itertools.product(syn, locations))))
    
    return garbage
    
