def ehPrimo(num):
    i = 2
    primo = True
    while ( i < num):
        if( num % i == 0):
            print("não primo")
            primo = False
            break
        i+=1
    if(primo):
        print("primo")

num = 1
while (num > 0):
    num = int(input("numero: "))
    ehPrimo(num)
