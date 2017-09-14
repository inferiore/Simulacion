i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
     31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
     60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
     89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
di = [0, 20, 45, 20, 30, 45, 25, 45, 40, 30, 40, 30, 40, 15, 40, 20, 40, 30, 45, 40, 15, 15, 30, 25, 30, 25, 45, 40, 35,
      25, 40, 20, 15, 30, 45, 30, 35, 35, 20, 40, 30, 45, 20, 40, 35, 45, 30, 20, 30, 45, 35, 45, 25, 25, 40, 25, 35,
      25, 15,
      35, 45, 40, 20, 30, 30, 25, 30, 35, 15, 20, 35, 20, 15, 25, 45, 20, 20, 15, 15, 15, 15, 40, 20, 40, 25, 20, 35,
      40, 25,
      15, 45, 40, 20, 20, 15, 15, 45, 35, 40, 20, 30]

oi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # order compras al proveedor

li = [200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # order compras al proveedor


sS = [25, 200]

def main():
    j = 0
    while (len(i)-1 > j):
        j = j + 1
        print("---------------"+" j:"+str(j)+"---------------------")
        print("li[j - 1]="+str(li[j - 1] )+" s="+str(sS[0]))
        if (li[j - 1] < sS[0]):
            print ("order")
            oi[j-1]=sS[1]-li[j-1]
        else:
            print("not order")
            oi[j] = 0
        print("li[j]="+"li[j - 1] + oi[j - 1] - di[j],"+ str(li[j - 1])+"+"+str(oi[j - 1])+"-"+str(di[j])+"="+str(li[j - 1] + oi[j - 1] - di[j]))
        li[j] = li[j - 1] + oi[j - 1] - di[j]
    oi[j] = sS[1] - li[j];
    li[j] = sS[1];
def getAverage(array):
   i = 0
   suma = 0
   average=0
   while ((len(array))>(i)):
       suma = array[i]+suma
       i = i + 1
       average=suma/(len(array))
   return average

def getAveragePositive(array):
   i = 0
   suma = 0
   average=0
   while ((len(array))>(i)):
       if(array[i]>0):
           suma = array[i] + suma
           i = i + 1

   average=suma/(i)
   return average

main()
print("inventory:" + str(li))
print("order:" + str(oi))
print("time:" + str(i))
print("demands:" +str(di))

print("average demands:" + str(getAverage(di)))
print("average order:" + str(getAverage(oi)))
print("average demands/per interval:" + str(getAverage(di)/len(di)))
print("average order/per interval:" + str(getAverage(oi)/len(di)))

print("costos por solo tener inventario:"+str(getAveragePositive(oi)))



