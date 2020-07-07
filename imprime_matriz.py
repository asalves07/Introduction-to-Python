def imprime_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (j+1) == len(m[i]):
                print(m[i][j], end="")
            else:
                print(m[i][j], end=" ")
        print()
