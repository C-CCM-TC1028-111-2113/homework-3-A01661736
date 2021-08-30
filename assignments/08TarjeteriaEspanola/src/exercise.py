def tarjetas(a,b):
    a*=12
    b*=35
    if (a>b):
        c=b
    elif (b>a):
        c=a
    return c

def main():
    print ("Dame la cantidad de pliegos de papel albanene")
    al=int(input())
    print ("Dame la cantidad de pliegos de plumones")
    pl=int(input())

    tarjetas(al,pl)
    T=tarjetas(al,pl)

    print ("Se pueden hacer: " + str(T) + " tarjetas")
    pass

if __name__=='__main__':
    main()
