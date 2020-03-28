# 4) Ordenar uma lista de nomes por ordem alfabética.
string = input("Informe os valores da lista: ").split(" ")
lista = []

for i in string:
    if not i.isalpha():     #se não for parte do alfabeto
        print("Digite apenas palavras!")
    elif i.isalpha():
        lista.append(i)
    
print(sorted(lista))
        
