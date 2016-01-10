## reverses a string w/o use of [::-1] or reversed

def reverse(string):
    x = int(len(string))
    y = ''
    for char in string:
        x-=1
        y+=y.join(string[x])
    return y    
        
reverse('Python!')
