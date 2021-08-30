def area(a,b):
    area=a*b
    return area



def main():
    print ("Dame el ancho del rectángulo")
    an=float(input())
    print ("Dame el alto del rectángulo")
    al=float(input())
    
    area(an,al)
    A=area(an,al)
    
    print("El área del rectángulo es: " + str(A) + " m^2")
    
    
    pass

if __name__=='__main__':
    main()
