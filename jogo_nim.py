     
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    terminou = False
    if (n % (m+1) != 0):
        print()
        print("Computador começa!")
        print()
        while(not terminou):
            comp = computador_escolhe_jogada(n, m)
            n -= comp
            if(n == 0):
                print("Fim do jogo! O computador ganhou!")
                terminou = True
                return True
            else:
                usu = usuario_escolhe_jogada(n, m)
                n -= usu
                if(n == 0):
                    print("Fim do jogo! Você ganhou!")
                    terminou = True
                    return False
    else:
        print()
        print("Voce começa!")
        print()
        while(not terminou):
            usu = usuario_escolhe_jogada(n, m)
            n -= usu
            if(n == 0):
                print("Fim do jogo! Você ganhou!")
                terminou = True
                return False
            else:
                comp = computador_escolhe_jogada(n, m)
                n -= comp
                if(n == 0):
                    print("Fim do jogo! O computador ganhou!")
                    terminou = True
                    return True
        
def computador_escolhe_jogada(n, m):
    if (n > m):
        q = (n % (m+1))
        if (q == 0):
            print("O computador tirou", m, "peça.")
            print("Agora resta apenas", n-m, "peça no tabuleiro.")
            print()
            return m
        else:
            print("O computador tirou", q, "peça.")
            print("Agora resta apenas", n-q, "peça no tabuleiro.")
            print()
            return q
    else:
        print("O computador tirou", n, "peça.")
        print("Agora resta apenas", n-n, "peça no tabuleiro.")
        print()
        return n
                
def usuario_escolhe_jogada(n, m):
    c = True
    while(c):
        x = int(input("Quantas peças você vai tirar? "))
        if(x > m or x > n or x <= 0):
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            c = True
        else: 
            print("Você tirou", x, "peças.")
            print("Agora resta apenas", n-x, "peça no tabuleiro.")
            print()
            c = False
    return x
    
def campeonato():
    y = 0
    x = 0
    print("**** Rodada 1 ****")
    print()
    z = partida()
    if (z):
        y = y + 1
    else:
        x= x+1
    print()
    print("**** Rodada 2 ****")
    print()
    z = partida()
    if (z):
        y = y + 1
    else:
        x= x+1
    print()
    print("**** Rodada 3 ****")
    print()
    z = partida()
    if (z):
        y = y + 1
    else:
        x= x+1
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você", x, "X", y, "Computador")

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
x = int(input("2 - para jogar um campeonato "))

if ( x == 1):
    print("Voce escolheu uma partida")
    print()
    partida()
else:
    print("Voce escolheu um campeonato!")
    print()
    campeonato()
