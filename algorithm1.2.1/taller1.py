
A= [1,4,11,12,17,9,18,6,10,15,19,13,20,3,14,8,2,5,7,16] #llegada original por si sirve de algo
a = [0,1,1,1,1,2,2,3,3,3,4,5,5,6,6,7,8,8,8,8] #tiempos de llegada
s = [4,3,3,5,3,5,3,4,3,5,2,4,3,4,1,4,1,2,5,4] #tiempos de servicio
d = [0,0,00,00,00,0,00,0,00,00,00,00,00,0,00,0,0,0,0,00] #Retrasos
c = [0,0,00,00,00,0,00,0,00,00,00,00,00,0,00,0,0,0,0,00] #departure time

averageArrival=0
averageService=0
averageDeparture=0
averageDelay=0


def main():
  i=-1
  while ((len(a))>=i+2):
      i=1+i
      print('------------------------' + str(i) + '-----------------------------')
      nextArrival=getArrival(i)
      #print ('Llega trabajo: '+str(a[i])+'. lo termino en: '+str(s[i])+'. el proxima trabajo llega en:'+str(nextArrival))

      if(nextArrival<getIndexNull(c,i-1)):
          #print ('existe un retraso de :'+str(getIndexNull(c,i-1)-nextArrival ))
          d[i] = getIndexNull(c,i-1)-nextArrival
      else:
          d[i]=0;
      nextService=getService(i)
      c[i]=nextArrival+d[i]+nextService
      #print('nextArrival:'+str(nextArrival)+' d['+str(i)+']:' +str(d[i])+' nextService:'+str(nextService))
      #print('no hay retraso, c['+str(i)+'] :' + str(c[i]))
      print('t llegada')
      print(a)
      print('t retraso')
      print(d)
      print('t servico')
      print(s)
      print('t salida')
      print(c)


def getArrival(i):
  return a[i]
def getService(i):
  return s[i]
def getIndexNull(array,index):
  try:
      return array[index]
  except IndexError:
      return 0
def getAverage(array):
   i = 0
   suma = 0
   average=0
   while ((len(array))>(i)):
       suma = array[i]+suma
       i = i + 1

       average=suma/len(array)
   return average

main()
averageArrival=getAverage(a)
averageService=getAverage(s)
averageDelay=getAverage(d)
averageDeparture=getAverage(c)

print('averageArrival:'+str(averageArrival))
print('averageService:'+str(averageService))
print('averageDelay:'+str(averageDelay))
print('averageDeparture:'+str(averageDeparture))

