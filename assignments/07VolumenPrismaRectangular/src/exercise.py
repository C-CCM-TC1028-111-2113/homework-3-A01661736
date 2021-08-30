
def area (a,b,c):
    
    Area=(a*b)*c
    return Area


def main():
    
    print ("Dame el ancho de la base")
    ba=float(input())
    print ("Dame el largo de la base")
    l=float(input())
    print ("Dame la altura del prisma")
    h=float(input())
    
    area(ba,l,h)
    Ar=area(ba,l,h)
    print ("El volumen es: " + str(Ar) +" m^3")
    
    pass

if __name__=='__main__':
    main()
