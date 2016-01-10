#function that takes a list of nums and outputs the even nums
def purify(lst):
    str1 = []
    for l in lst:
        if l % 2 > 0:
            print l
        else:
            str1.append(l)
    return str1        
