from __future__ import division
import math

def binomial(n,p,x):
   return  (math.factorial(n)/(math.factorial(x)*math.factorial(n-x))) *  (p**x)*(1-p)**(n-x)

print (binomial(5,0.5,0))
print (binomial(5,0.5,1))
print (binomial(5,0.5,2))
print (binomial(5,0.5,3))
print (binomial(5,0.5,4))
print (binomial(5,0.5,5))








