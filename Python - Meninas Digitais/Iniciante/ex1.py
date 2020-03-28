#1) Adivinhar o número: sorteie um número e faça o jogador adivinhar que número é esse.

from random import randint
aleatorio = randint(0,9)
for t in range(6):
    numero = int(input("Escolha um numero de 0 a 9: "))
    if(numero != aleatorio):
        print("VOCE ERROU! Tente novamente.")
    elif(numero == aleatorio):
        print("Voce acertou!")
        break
print("Acabaram suas chances!")
