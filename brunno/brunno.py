import numpy
from mpmath import *
from scipy import integrate
from scipy import special




#constante de catalan



#serie de maclaurin
def mac(s):
	n = 0
	for i in range(1,1000):
		n+=(s)**i/fat(i)
	return n
	
'''
if __name__ == '__main__':
	print(atez(7))
'''


