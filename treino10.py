import random
import string

# Passo 1: perguntar o tamanho da senha
tamanho = int(input("Quantos caracteres sua senha deve ter? "))

# Passo 2: definir os possíveis caracteres da senha
letras = string.ascii_letters  # abc...XYZ
numeros = string.digits        # 0123456789
simbolos = string.punctuation  # !@#$%&*()

# Juntar tudo em uma só lista
todos_caracteres = letras + numeros + simbolos

# Passo 3: gerar a senha
senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))

# Passo 4: mostrar a senha
print("🔐 Sua senha gerada é:", senha)
