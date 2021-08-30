def bisiesto(a):
    bis=False
    if (a%4==0):
        bis=True
    elif (a%100==0)and(a%400==0):
        bis=True
    return  bis

def main():
    #escribe tu código abajo de esta línea
    print ("Dame el año")
    inpu=int(input())

##bisiesto(inpu)
        
    L=bisiesto(inpu)

    print (str(L))
    pass

if __name__=='__main__':
    main()
