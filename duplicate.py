#function that takes list of nums as input and outputs list minus duplicate nums
def remove_duplicates(lst):
    new = []
    for l in lst:
        if l in new:
            print l
        else:
            new.append(l)
    return new    
