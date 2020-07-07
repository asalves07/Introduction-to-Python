import math

def delta(a, b, c):
    return (b ** 2) - 4 * a * c

def Raizes(a, b, c):
    d = delta(a, b, c)
    if (d == 0):
        raiz1 = (-b + math.sqrt(d))/(2 * a)
        print("a raiz desta equação é", raiz1)  
    else:
        if (d<0):
            print("esta equação não possui raízes reais")
        else:
            x = (-b + math.sqrt(d))/(2 * a)
            y = (-b - math.sqrt(d))/(2 * a)
            if(x < y):
                print("as raízes da equação são", x, "e", y)
            else:
                print("as raízes da equação são", y, "e", x)
                
def main():
    a = float(input())
    b = float(input())
    c = float(input())
    Raizes(a, b, c)



