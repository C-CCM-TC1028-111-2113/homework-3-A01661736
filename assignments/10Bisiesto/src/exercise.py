def bisiesto(a):
    
    if (a/4==0):
        a==True
        

    if (a/4==0 )and(a/100==0):
        if (a/400==0):
            a==True
          
        else:
            a==False
            
    b=print(str(a))
    return  b

def main():
    #escribe tu código abajo de esta línea
    print ("Dame el año")
    inpu=int(input())

    bisiesto(inpu)
    L=bisiesto(inpu)

    print (str(L))
    pass

if __name__=='__main__':
    main()
