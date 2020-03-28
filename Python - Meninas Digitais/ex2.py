# 2) Gerar a sequência de Collatz. Esta sequência consiste em escolher um número
numero = int(input("Informe um numero grande para dar inicio a Sequencia de Collatz: "))
while numero < 100:
    numero = int(input("Informe um numero grande para dar inicio a Sequencia de Collatz: "))

lista = []
lista.append(numero)

while numero != 1:
    if numero % 2 == 0:
        numero /= 2
        lista.append(numero)
        
    elif numero % 2 != 0:
        numero = (numero * 3) + 1
        lista.append(numero)

print(lista)

