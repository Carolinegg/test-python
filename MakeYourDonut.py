coberturas = ["chocolate", "calda de morango", "pasta de amendoim"]
sabores = ["chocolate", "red velvet", "vegano", "normal"]
escolhas_granulado = ["com", "sem"]


def saudar():
    print("Bem vindo ao Carolineas Donuts, qual seria seu pedido?")


def mostrar_sabores():
    # tem que mostrar por exemplo "1 - opção"
    for index, sabor in enumerate(sabores):
        print(str(index) + " - " + sabor)


def mostrar_coberturas():
    # também mostra exemplos de opções "1 - opção"
    for index, cobertura in enumerate(coberturas):
        print(str(index) + " - " + cobertura)


def pedir():
    print("Temos varias opções de sabores, tamanhos, coberturas, com ou sem granulado e quantidade.\n")
    # variavel = expressao_de_func
    sabor = pedir_sabor()

    print("\nCerto! E a cobertura qual seria? \n")

    cobertura = pedir_cobertura()

    tamanho = pedir_tamanho()

    print("Ótimo!")

    granulado = pedir_granulado()

    print("Certo!")

    quantidade = pedir_quantidade()

    print("Perfeito! Seu pedido está pronto!")

    return [sabor, cobertura, tamanho, granulado, quantidade]


def pedir_quantidade():

    quantidade = ''
    while True:
        quantidade = input(
            "\nE por último, quantas unidades você gostaria deste donut? (Pode-se encomendar até 50 un) ")

        if validar_quantidade(quantidade):
            break

        print("Desculpe mas não possuimos essa quantidade no estoque hoje")

    return quantidade


def pedir_granulado():

    granulado = ''
    while True:
        granulado = input("\nE você gostaria com ou sem granulado?  ")

        if validar_granulado(granulado):
            break

        print("Opção incorreta.")

    return granulado


def pedir_tamanho():
    print("\nAgora podemos escolher o tamanho, ela varia de 10 a 30 cm.")

    tamanho = ''
    while True:
        tamanho = input("\nDe quantos cm seria o tamanho do seu donut? ")

        if validar_tamanho(tamanho):
            break

        print("Poderia informar corretamente o tamanho do seu donut novamente por favor? ")

    return tamanho


def pedir_cobertura():
    mostrar_coberturas()

    cobertura = ''
    while True:
        cobertura = input("\nDigite o sabor da cobertura: ")

        if validar_cobertura(cobertura):
            break

        print("Desculpe mas ainda não temos este sabor de cobertura.")

    return cobertura


def pedir_sabor():
    mostrar_sabores()

    sabor = ''
    while True:
        sabor = input("\nQual o sabor da massa: ")

        if validar_sabor(sabor):
            break

        print("Perdão mas este sabor de massa não temos na loja.")

    return sabor


def validar_sabor(sabor: str):
    if sabor.lower() in sabores:
        return True

    if sabor.isdigit() and len(sabores) > int(sabor):
        return True

    return False


def validar_tamanho(tamanho: str):
    if not tamanho.isdigit():
        return False

    tam = int(tamanho)

    if tam < 10:
        print("Desculpe, mas o tamanho deve ser maior que 10 cm!")
        return False

    if tam > 30:
        print("Desculpe, mas o tamanho deve ser menor que 30 cm!")
        return False

    return True


def validar_cobertura(cobertura):
    if cobertura.lower() in coberturas:
        return True

    if cobertura.isdigit() and len(coberturas) > int(cobertura):
        return True

    return False


def validar_granulado(granulado: str):
    if granulado.lower() in escolhas_granulado:
        return True

    return False


def validar_quantidade(quantidade):
    if not quantidade.isdigit():
        return False

    qnt = int(quantidade)

    if qnt >= 50:
        return False

    return True


def mostrar_resultado(pedido):
    sabor = pedido[0]
    cobertura = pedido[1]
    tamanho = pedido[2]
    granulado = pedido[3]
    quantidade = pedido[4]

    print(
        f"Seu donut de {sabor} com cobertura de {cobertura} no tamanho {tamanho} cm, {granulado} granulado e {quantidade} unidades!")
    print("Obrigada pelo pedido e volte sempre!")


def main():
    saudar()
    pedido = pedir()
    mostrar_resultado(pedido)


if __name__ == "__main__":
    main()
