file = open("newfile.txt", "w")
file.write("This is a text file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

# Quando um arquivo é aberto em write mode o conteúdo do arquivo existente é excluído (Se abrir um arquivo em write mode e imediatamente fechá-lo o conteúdo será DELETADO)
file = open("newfile.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

msg = "Hey soul sister!"
file = open("newfile.txt", "w")
about = file.write(msg)
print(about)
file.close()

# Para evitar perdas tendo a certeza que os arquivos serão sempre fechados depois de serem usados. Ou pode-se usar o with também.
try:
    file = open("blabla.txt")
    print(file.read())
finally:
    file.close()

with open("Iknowaboutthat.txt") as f:
    print(f.read())
