v = []
ind = False
i=0
while(not ind):
    v.append(int(input()))
    if(v[i] == 0):
        ind = True
    i+=1
i-=1
while(i >0):
    i -=1
    print(v[i])
    
    
