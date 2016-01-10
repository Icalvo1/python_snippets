## function returns all vowels from str
def anti_vowel(text):
    sto = ''
    for l in text:
        if l in 'aeiouAEIOU':
            sto+= sto.join(l)
        else:
            print l
    return sto        
    
