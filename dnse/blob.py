from wordsegment import load, segment
import itertools

def exact_check(inlist, orig):
    ende = []
    for x in inlist:
        if x != orig:
            ende.append(x)
    return ende

def check_data(alist):
    replist = [];
    for x in alist:
        y = x
        y += '.'
        fail = False
        fin = open('zonedata', 'r').readlines()
        for line in fin:
            if y in line:
                fail = True

        fin = open('Reserved', 'r').readlines()
        for line in fin:
            if x in line:
                fail = True
        if fail == False:
            replist.append(x)
    return replist

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

def combine_all(locations, syn, tldd, addtld):
    garbage = list(map(''.join, itertools.chain(itertools.product(locations, syn), itertools.product(syn, locations))))
    garbage += list(map(''.join, itertools.chain(itertools.product(syn, syn))))
    garbage += syn;
    if addtld == True:
        topGarbage = list(map('.'.join, itertools.chain(itertools.product(garbage,tldd))))
    else:
        topGarbage = garbage

    return topGarbage
    
