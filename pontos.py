import math

x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())

D = math.sqrt(((x1 - x)**2)+((y1 -y))**2)



if(D >= 10):
    print("longe")
else:
    print("perto")
