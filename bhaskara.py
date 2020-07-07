import math

a = float(input())
b = float(input())
c = float(input())


D = b ** 2 - 4 * a * c

if (D == 0):
    raiz1 = (-b + math.sqrt(D))/(2 * a)
    print("a raiz desta equação é", raiz1)
             
else:
    if (D<0):
        print("esta equação não possui raízes reais")
    else:
        x = (-b + math.sqrt(D))/(2 * a)
        y = (-b - math.sqrt(D))/(2 * a)
        if(x < y):
            print("as raízes da equação são", x, "e", y)
        else:
            print("as raízes da equação são", y, "e", x)
