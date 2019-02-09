def greet():
    enter = str(input('\nBem vindo ao jogo da velha! Vamos jogar? \nAbaixo escolha como player x ou o:'))

    if enter not in "x" or "o":
        print("Ocorreu um erro, escolha corretamente")

    return greet()


def show_board():
    board = [[0 for i in range (3)] for j in range (3)]

#mostrar q os zeros sao espacos em branco e tenho q definir coluna e linha

    print(board)

def players():

    p1 = 1
    p2 = 2

    if p1 in show_board:
        print("x")

    if p in show_board:
        print("o")


def start():
    pass
#Onde esta x nao pode o e visse versa.

def win_or_stuck():
    pass

def main():
    greet()
    show_board()
    players()
    start()
    win_or_stuck()
    main()
