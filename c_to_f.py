##function that converts degrees C to degrees F
##f(x) = 9x/5 + 32
from __future__ import division
def f():
	c_input = float(raw_input('Enter a temperature in Celsius: '))
	print str(c_input) + ' Degrees Celsius is ' + str(9*c_input/5 + 32) + ' Degrees Fahrenheit'
	ag()
def ag():
	again = raw_input('\nAgain? enter "y" for yes or "n" for no:  ')
	if again == 'y'.lower():
		f()
	else:
		quit()	
f()