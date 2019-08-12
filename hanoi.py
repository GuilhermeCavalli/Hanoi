pilha1 = ['bloco 3','bloco 2','bloco 1']
pilha2 = []
pilha3 = []
def mostra():
    print('haste 1: ',pilha1)
    print('haste 2: ',pilha2)
    print('haste 3: ',pilha3)
def mover():
    tirar=int(input('Escolha uma haste para REMOVER o bloco: '))
    if tirar == 1:
        if len(pilha1) != 0:
            inp= pilha1.pop()
            ir=int(input('Escolha a uma haste para COLOCAR o bloco: '))
            if ir == 1:
                if len(pilha1) == 0 or pilha1[0] > inp:
                    pilha1.append(inp)
                else:
                    pilha1.append(inp)
                    print('PRA QUE MOVEU ENTAO SEU INCEFALO')
            elif ir == 2:
                if len(pilha2) == 0 or pilha2[0] > inp:
                    pilha2.append(inp)
                else:
                    pilha1.append(inp)
                    print('TESTE ERRO')
            elif ir == 3:
                if len(pilha3) == 0 or pilha3[0] > inp:
                    pilha3.append(inp)
                else:
                    pilha1.append(inp)
                    print('TESTE ERRO')
            else:
                print('A haste nao existe')
                pilha1.append(inp)
        else:
            print('haste vazia')
    elif tirar == 2:
        if len(pilha2) != 0:
            inp= pilha2.pop()
            ir=int(input('Escolha a uma haste para COLOCAR o bloco: '))
            if ir == 1:
                if len(pilha1) == 0 or pilha1[0] > inp:
                    pilha1.append(inp)
                else:
                    pilha2.append(inp)
                    print('TESTE ERRO')
            elif ir == 2:
                if len(pilha2) == 0 or pilha2[0] > inp:
                    pilha2.append(inp)
                else:
                    pilha2.append(inp)
                    print('TESTE ERRO')
            elif ir == 3:
                if len(pilha3) == 0 or pilha3[0] > inp:
                    pilha3.append(inp)
                else:
                    pilha2.append(inp)
                    print('TESTE ERRO')
            else:
                print('A haste nao existe')
                pilha2.append(inp)
        else:
            print('haste vazia')
    elif tirar == 3:
        if len(pilha3) != 0:
            inp= pilha3.pop()
            ir=int(input('Escolha a uma haste para COLOCAR o bloco: '))
            if ir == 1:
                if len(pilha1) == 0 or pilha1[0] > inp:
                    pilha1.append(inp)
                else:
                    pilha3.append(inp)
                print('TESTE ERRO')
            elif ir == 2:
                if len(pilha2) == 0 or pilha2[0] > inp:
                    pilha2.append(inp)
                else:
                    pilha3.append(inp)
                    print('TESTE ERRO')
            elif ir == 3:
                if len(pilha3) == 0 or pilha3[0] > inp:
                    pilha3.append(inp)
                else:
                    pilha3.append(inp)
                    print('TESTE ERRO')
            else:
                print('A haste nao existe')
                pilha3.append(inp)
        else:
            print('haste vazia')
    else:
        print('A haste nao hexiste')

def PLAYGAME():        
    jogando = True
    while jogando:
        mostra()
        mover()
        if pilha3 == ['bloco 3','bloco 2','bloco 1']:
            print('0----------------------------------------0')
            print('| Parabens, você é um genio! Seja Feliz! |')
            print('0----------------------------------------0\n')
            jogando = False
        else:
            jogando = True
