from wordsegment import load, segment

def strip_out(name):
    cleared = str.replace(name, "*", "")
    cleared = str.replace(cleared, " ", "")
    cleared = str.replace(cleared, "-", "")
    cleared = str.replace(cleared, ".", "")
    return cleared

