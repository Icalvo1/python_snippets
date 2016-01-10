#function that returns the number of times a number appears in list
def count(sequence, item):
    x = 0
    for i in sequence:
        if i == item: 
            x+=1
    return x    
