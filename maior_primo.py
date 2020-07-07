def éPrimo(num):
    i = 2
    primo = True
    while ( i < num):
        if( num % i == 0):
            return False
            primo = False
            break
        i+=1
    if(primo):
        return True

def maior_primo (num):
    x = 2
    while (x <= num):
        if(éPrimo(x)):
            maior = x
        x+=1
    return maior
    
