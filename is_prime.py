##function to check if x is prime or not
## src = http://linuxconfig.org/function-to-check-for-a-prime-number-with-python

def is_prime(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	    return False
    return True

'''
def num_inp():
    num_chk = raw_input('enter a number to check: ')
    return is_prime(int(num_chk))	
num_inp()
'''
x = int(raw_input('enter a num: '))
print is_prime(x)  
raw_input()