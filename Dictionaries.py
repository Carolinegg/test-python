ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

# Quando não ha valor pré-definido, e você define depois, é adicionado a frente dos outros valores?

squares = {1: 1, 2: 4, 3: "vish", 4: 8}
squares[8] = 46
squares[3] = 6
print(squares)

# Determinar se uma chave esta dentro do dicionário usar in ou not in.

nums = {1: "one", 2: "two", 3: "three"}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
