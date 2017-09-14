a = [15,47,71,111,123,152,166,226,310,320] #tiempos de llegada
s = [43,36,34,30,38,40,31,29,36,30] #tiempos de servicio
d = [0,0,0,0,0,0,0,0,0,0] #Retrasos
c = [0,0,0,0,0,0,0,0,0,0] #departure time

def main():
    i=-1
    while ((len(a))>=(i-2)):
        i=1+i
        nextArrival=getArrival(i)
        print ('Llega trabajo: '+str(a[i])+'. lo termino en: '+str(s[i])+'. el proxima trabajo llega en:'+str(nextArrival))

        if(nextArrival<getIndexNull(c,i-1)):
            print ('existe un retraso de :'+str(getIndexNull(c,i-1)-nextArrival ))
            d[i] = getIndexNull(c,i-1)-nextArrival
        else:
            d[i]=0;
        nextService=getService(i)
        c[i]=nextArrival+d[i]+nextService
        print('nextArrival:'+str(nextArrival)+' d['+str(i)+']:' +str(d[i])+' nextService:'+str(nextService))
        print('no hay retraso, c['+str(i)+'] :' + str(c[i]))
        print ('-----------------------------------------------------')
        print(a)
        print(d)
        print(s)
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
main()
