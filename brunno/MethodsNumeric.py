import mpmath as mp
import random as rd
print('oi')
class NewtonRaph:
	def __init__(self, fun, n, err=(15)):
		self.fun = fun
		self.n = n
		self.error = []
		self.xlist = []
		self.n = []
		i = 1
		#iterative loop
		x = rd.random()
		while(True):
			 i += i
			 x = x - (fun(x)-n)/mp.diff(fun,x)
			 self.xlist.append(x)
			 #print(x)
			 e = fun(x) - n
			 self.error.append(e)
			 #print(e)
			 self.n.append(i)
			 if(e < 10**(-err)):
			 	break
			 else:
			 	continue
		self.x = x
		
class Euler:
	def __init__(self, df, n, h=0.01):
		self.y = 1
		self.x = 0
		self.listy = []
		self.listn = []
		self.listx = []
		for i in range(n):
			self.y = self.y + h*df(self.x,self.y)
			self.listy.append(self.y)
			self.listn.append(i)
			self.listx.append(self.x)
			self.x += h
		
'''
f = (lambda x:( x**2))
p = Newton(f, 5)
print(p.x)
print(diff(f,3))
print(Newton(gamma, pi).xlist)
print(Newton(gamma, euler+1).add(4))
'''