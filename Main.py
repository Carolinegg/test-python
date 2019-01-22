
def main():
    while True:
        try:
            tamanho_casa = input('Digite o tamanho da casa (deve ser maior que 0): ')
            sucesso = criar_casa('rosa', tamanho_casa)

            if sucesso:
                break

        except Exception as err:
            print("Um erro ocorreu!\n\n Erro: {}".format(err))

def criar_casa(cor, tamanho):
    quadrado = criar_quadrado(tamanho)
    mudar_cor_quadrado(quadrado, cor)

    return True

def criar_quadrado(tamanho):
    t = int(tamanho)
    if t <= 0:
        raise Exception("Tamanho inválido")
    return { 'tamanho': t, 'cor': 'preto' }
    
def mudar_cor_quadrado(quadrado, cor):
    pass

main()
