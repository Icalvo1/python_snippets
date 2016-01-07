## return x/2 in decimal format
from __future__ import division
def f(x):
	if x > 0:
		return 1/x
def num():		
	num = int(raw_input('\nEnter a number x to divide by 1(ex: 1/x): '))
	if num == int(num):
	num = f(num)
	print num
	ag()
def ag():
	again = raw_input('\nAgain? enter "y" for yes or "n" for no:  ')
	if again == 'y'.lower():
		num()
	else:
		quit()
num()
