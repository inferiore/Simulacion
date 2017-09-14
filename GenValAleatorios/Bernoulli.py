from random import random

result=[]
def BernoulliRandomVariate():
   if(random()<(1-0.8)):
       result.append(0)
       return (0)
   else:
       result.append(1)
       return (1)

i=0
while (True):
   i=i+1
   BernoulliRandomVariate()
   if(i==10000):
       break

def sumarLista(lista):
   sum=0
   for i in range(0,len(lista)):
       sum=sum+lista[i]

   return sum
print ("result:"+str((result)))
print ("suma:"+str(sumarLista(result)))
print ("promedio:"+str(sumarLista(result)/len(result)))


