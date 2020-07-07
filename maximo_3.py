def maximo(x, y, z):
    if x < y and y > z:
        return y
    else:
        if (x > y and x > z):
            return x
        else:
            return z 
