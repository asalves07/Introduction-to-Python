l = int(input())
a = int(input())

i=1
while(i <= a):
    j = 2
    print("#", end = "")
    while(j < l):
        if(i == 1 or i == a):
            print("#", end = "")
        else:
            print(" ", end = "")
        j+= 1
    print("#", end = "")
    print()
    i+=1
