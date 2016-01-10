# function that takes a string and a target word, then censors the target word in the # string
def censor(string, word):
    ar = string.split()
    for v in ar:
        if v == word:
            lng = len(v)
            idx = int(ar.index(v))
            ar[idx] = '*' * lng
            print ar[idx]
    return " ".join(ar) 
