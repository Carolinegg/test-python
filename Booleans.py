my_b = True
print(my_b)

print(2 == 3)

# Podem haver dois valores: True ou False, para a comparação dos valores utiliza-se ==.
print("hello" == "hello")

# Para a comparação de valores NÃO IGUAIS. Ou seja, se os itens comparados forem diferentes o resultado é True.
print("eleven" != "seven")

# Para opecações com NÚMEROS (floats e integers) os símbolos de comparação são o maior que e menor que (com ou sem igual).
print(7 > 5)

print(10 < 10)

print(7 >= 8)

# AND ou & : precisa de dois argumentos, apenas se os dois argumentos forem verdadeiros -> True

print(1 == 1 and 3 == 3)
print(1 != 1 and 2 == 2)

# OR leva dois argumentos, se um ou dois argumentos forem verdadeiros -> True e False se os dois forem falsos

if (1 == 1 or 2 == 2):
    print("true story")

if (2 == 1 or 3 > 6):
    print("false story")

# NOT requer apenas um argumento no qual inverte-se: o resultado de not True é False e not False será True

y = not 1 == 1
print(y)

x = not 1 > 7
print(x)
