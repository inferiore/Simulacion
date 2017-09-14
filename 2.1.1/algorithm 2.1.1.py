def isFullPeriod (m,a):
    var = False
    p = 1;
    x = a;
    if(a==m):
        exit(1)
    while (x != 1):
        p=p+1
        x = (a * x)% m #/* beware of a ∗ x overflow */
    if (p == (m - 1)):
        var=True
        #print(str(a)+":full-period multiplier")
    return var
fullPeriods=[]#[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]

def main (m,numeros):

    i=0
    while(m>i):
        i=i+1
        #print(isFullPiriod(m,i));
        if (isFullPeriod(m, i) == True):
            (numeros.append(i))
            print(i)
    fullPeriods=numeros
    print((fullPeriods))
    #return fullPeriods
if __name__ == '__main__':
    (main(127,fullPeriods))
    print(fullPeriods)