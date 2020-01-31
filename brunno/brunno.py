import numpy as np
from mpmath import *
from scipy import special

mp.pretty = True

H = harmonic
y = euler

#funcoes

#zeta
	
def rim(s):
	return 1+nsum(lambda u:(power(-log(u),u)*power(s,u)*(1/gamma(u+1))),[1,inf])

#Dirichet
def dirichet(s):
	return nsum(lambda n:(power(-1,n)*power(2*n+1,-s)),[0,inf])

#eulermasqerony
def eulermasc(a,x):
	return quad(lambda t:exp(-t)*power(t,a-1),[0,x])
	
#funcao de eta dirichlet
def eta(s):
	return (nsum(lambda u: power(-1,u+1)/power(u,s),[1,inf]))

#funcao transcendental de lerch
def lerch(z,s,a):
	return nsum(lambda n:power(z,n)/power(n+a,s),[0,inf])

#funcao zeta de hurwitz
def hurwitz(s,q):
	return nsum(lambda k:1/power(k+q,s),[0,inf])

#Polilogaritmo
def L(s,z):
	return nsum(lambda k:power(z,k)/power(k,s),[0,inf])
	
#integral of euler-maskeroni
def em(n,z):
	return quad(lambda t:exp(t*n)/power(t,n),[0,inf])

#Hermite
def hermite(n,x):
	return (power(-1,n)*exp(power(x,2))*diff(lambda u:(exp(power(-u,2))),x))

#dfrac
def difrac(fun, x, n=1/2):
	iii = lambda s:(quad(lambda t:(fun(t)/power((s-t),n)),[0,s]))
	return (1/gamma(1-n))*diff(iii ,x)

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



