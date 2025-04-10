#criou um arquivo .txt
with open("dados.txt", "w") as arquivo:
    arquivo.write("Olá, esse é um teste!\n")
    arquivo.write("Aprendendo a manipular arquivos em Python.")

#leu o arquivo,O modo "r" é usado para leitura.
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
#usamos o modo "a" (append) para adicionar novas linhas.
with open("dados.txt", "a") as arquivo:
    arquivo.write("\n Ola mundo!")
