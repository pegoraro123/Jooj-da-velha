tabuleiro = [ [0 for i in range(3)] for j in range(3)]#cria tabuleiro
def menu():#define menu para iniciar o jogo
    continuar=1
    while continuar:
        continuar = int(input("1. Sair \n"+
                              "2. Jogar\n"))
        if continuar:
            game()#chama a função game para executar o programa
        else:
            print("Passar bem!!!")#se o usuário sair  encerra o programa

def game():#define jogadas possiveis
    jogada=0

    while ganhou() == 0:#repete a função ganhou se for igual a 0
        print("\nJogador ", jogada%2 + 1)
        exibe()#chama a função exibe 
        linha  = int(input("\nLinha :"))#interege com o usuário
        coluna = int(input("Coluna:"))

        if tabuleiro[linha-1][coluna-1] == 0:
            if(jogada%2+1)==1:
                tabuleiro[linha-1][coluna-1]=1
            else:
                tabuleiro[linha-1][coluna-1]=-1
        else:
            print("Nao esta vazio")
            jogada -=1

        if ganhou():
            print("Jogador ",jogada%2 + 1," ganhou apos ", jogada+1," rodadas")

        jogada +=1
    
def ganhou():#define vitória
    #checa linhas
    for i in range(3):
        soma = tabuleiro[i][0]+tabuleiro[i][1]+tabuleiro[i][2]
        if soma==3 or soma ==-3:
            return 1

     #checa as colunas
    for i in range(3):
        soma = tabuleiro[0][i]+tabuleiro[1][i]+tabuleiro[2][i]
        if soma==3 or soma ==-3:
            return 1

    #checa as diagonais
    diagonal1 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0

def exibe():#define a função que exibe o tabuleiro na tela 
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                print(" _ ", end=' ')
            elif tabuleiro[i][j] == 1:
                print(" X ", end=' ')
            elif tabuleiro[i][j] == -1:
                print(" O ", end=' ')
#layout
        print()
                
tabuleiro= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]#faz cada indice do tabuleiro ficar vazio

menu()#chama o menu
