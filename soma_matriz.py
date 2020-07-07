def soma_matrizes(m1, m2):
    m =[]
    lin1 = len(m1)
    col1 = len(m1[0])
    lin2 = len(m2)
    col2 = len(m2[0])
    if (lin1 == lin2) and (col1 == col2):
        for i in range(len(m1)):
            linha =[]
            for j in range(len(m1[i])):
                linha.append(m1[i][j] + m2[i][j])
            m.append(linha)
        return m
    else:
        return False
