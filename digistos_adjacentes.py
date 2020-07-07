num = int(input())
t = len(str(num))
adjacente = False
aux = num % 10
while(num != 0 and not adjacente):
    num = num // 10
    aux2 = num % 10
    if (aux == aux2):
        adjacente = True
    else:
        aux = aux2
if (adjacente):
    print("sim")
else:
    print("não")
        
