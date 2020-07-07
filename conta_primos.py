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

def n_primos(num):
    x = 2
    n = 0
    while (x <= num):
        if(éPrimo(x)):
            n +=1
        x+=1
    return n
    
