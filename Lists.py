words = ["hello", "word", "!"]
print(words[0])
print(words[2])
num = "hey"
things = ["a", num, 2, 3]
print(things[0])

# List Operations

nums = [4, 4, 4, 4]
nums[3] = 8
print(nums)

# in operator: checa se esta na lista. Se for verdade retorna para True se não existir será False

flavor_pizza = ["egg", "cheese", "pepperoni", "tomato", "oregano"] 
print("egg" in flavor_pizza)
print("apple" in flavor_pizza)

# List Functions - método append: para adicionar um item no final da lista existente

alfabeto = ["a", "b", "c"]
alfabeto.append("d")
print(alfabeto)

# len function: a função len diferente da lista, inicia pelo 1 não pelo 0 (ela é utilizada fora da lista)

quantos = [2, 4, 6, 8, 10, 12]
print(len(quantos))

# insert method: similar ao append, porém você pode inserir um novo item em qualquer lugar da lista

here = ["Amsterdam", "goed"]
index = 1
here.insert(index, "ist")
print(here)

# index method: procura a primeira ocorrência do item na lista e retorna o index

letters = ['p', 'q', 'r', 's', 'p']
print(letters.index('p'))
print(letters.index('q'))

# range function: cria uma lista de sequência numérica. Se houver dois argumentos significa que você quer de um número, até outro. Se houver três argumentos o TERCEIRO argumento determina o intervalo da sequência entre os dois numeros.

numbers = list(range(10))
print(numbers)

ya = list(range(3,8))
print(ya)

oi = list(range(5, 20, 2))
print(oi)
