from wordsegment import load, segment
from string import maketrans

def strip_out(name):
    bad_char = ".-"
    gud_char = "  "
    tranab = maketrans(bad_char, gud_char)
    cleared = name.translate(tranab)
    cleared = cleared.replace(" ", "")
    return cleared

def give_list(block):
    return segment(block)
