def remove_repetidos(lista):
    lista.sort()
    aux = lista[0]
    l=[]
    l.append(aux)
    for x in range(0, len(lista)):
        if(aux != lista[x]):
            aux = lista[x]
            l.append(aux)
    return l
