i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # times ejecuciones
di = [0, 30, 15, 25, 15, 45, 30, 25, 15, 20, 35, 20, 30]  # demand compras de clientes
oi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # order compras al proveedor
li = [60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # inventory existencias
sS = [20, 60]
j = 0
while (len(i)-1 > j):
    j = j + 1
    print("---------------"+" j:"+str(j)+"---------------------")
    print("li[j - 1]"+str(li[j - 1] )+" s:"+str(sS[0]))
    if (li[j - 1] < sS[0]):
        print ("order")
        oi[j-1]=sS[1]-li[j-1]
    else:
        print("not order")
        oi[j] = 0
    print("li[j]="+"li[j - 1] + oi[j - 1] + di[j]:"+ str(li[j - 1])+"+"+str(oi[j - 1])+"-"+str(di[j]) )
    li[j] = li[j - 1] + oi[j - 1] - di[j]
oi[j] = sS[1] - li[j];
li[j] = sS[1];

print("inventory:"+str(li))
print("order"+str(oi))
print("demands"+str(di))
def getAverage(array):
   i = 0
   suma = 0
   average=0
   while ((len(array))>(i)):
       suma = array[i]+suma
       i = i + 1
       average=suma/(len(array))
   return average,suma
del(di[0])
del(oi[0])
print("average demands:" + str(getAverage(di)))
print("average order:" + str(getAverage(oi)))


