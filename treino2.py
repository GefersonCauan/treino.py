import random

numero_secreto = random.randint(1, 100)
tentativas = 0 

print("bem vindo ao jogo de adivinhaçao!")
print("tente adivinhar o numero que eu estou pensando (entre 1 e 100).")

while True:
    palpite = int(input("digite seu palpite:"))
    tentativas += 1 
    

    if palpite < numero_secreto:
        print("muito baixo! tente novamente")
    elif palpite > numero_secreto:
        print("muito alto! tenete novamente")
    else:
        print(f"parabens vc acertou o numero {numero_secreto} em {tentativas} tentativas.")
        break        