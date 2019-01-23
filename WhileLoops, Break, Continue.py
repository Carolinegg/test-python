# While é similar ao if (funciona se for True e não ocorre se for False) a diferença é que ele ele não corre apenas uma vez mas repetidas vezes. Uma vez que a avaliação é falsa a próxima sessão do código é executada

i = 1
while 1 >= 5:
    print(i)

i = i + 1

print("Finished")

# Para terminar um while loop antecipadamente o break pode ser usado

i = 0

while 1 == 1:
    print(i)
    i = i + 1

    if i >= 5:
        print("Breaking")
        break
print("Done!")

# Continue: ao contrário do break o continue pula de volta ao topo do loop ao invés de parar ele

i = 0

while True:
    i = i + 1

    if i == 2:
        print("Hi there!")
        continue

    if i == 5:
        print("Breaking")
        break
    print(i)
print("Finished")
