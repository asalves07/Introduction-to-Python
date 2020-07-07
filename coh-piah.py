import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    valor = 0
    for x in range(len(as_a)):
        f = as_a[x] - as_b[x]
        if f < 0:
            f*=(-1)
        valor += f
    return valor/6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinaturas = []
    sentencas = separa_sentencas(texto)
    palavras = lista_palavras(sentencas)
    assinaturas.append(wal(palavras))
    assinaturas.append(ttr(palavras))
    assinaturas.append(hlr(palavras))
    assinaturas.append(sal(sentencas))
    assinaturas.append(sac(sentencas))
    assinaturas.append(pal(sentencas))
    return assinaturas

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    infect = []
    for x in range(len(textos)):
        infect.append(compara_assinatura(ass_cp, calcula_assinatura(textos[x])))
    text = infect[0]
    texto = 1
    for x in range(1, len(infect)):
        if infect[x] < text:
            text = infect[x]
            texto+=1
    return texto

def lista_palavras(sentencas):
    frases=[]
    palavras=[]
    for x in sentencas:
        f = separa_frases(x)
        frases = frases + f
    for x in frases:
        p = separa_palavras(x)
        palavras = palavras + p
    return palavras
        
def wal(palavras):
    tam = 0
    for x in palavras:
        tam += len(x)
    return tam / len(palavras)

def ttr(palavras):
    n_dif = n_palavras_diferentes(palavras)
    return n_dif / len(palavras)

def hlr(palavras):
    n_uni = n_palavras_unicas(palavras)
    return n_uni / len(palavras)

def sal(sentencas):
    total = 0
    for x in sentencas:
        total += len(x)
    return total / len(sentencas)

def sac(sentencas):
    frases=[]
    for x in sentencas:
        f = separa_frases(x)
        frases = frases + f
    return len(frases)/len(sentencas)

def pal(sentencas):
    frases=[]
    total = 0
    for x in sentencas:
        f = separa_frases(x)
        frases = frases + f
    for x in frases:
        total += len(x)
    return total/len(frases)

assinatura = le_assinatura()
textos = le_textos()
texto = avalia_textos(textos, assinatura)
print("O autor do texto", texto, "está infectado com COH-PIAH")
