"""
6) Escrever uma função que imprime um inventário de um personagem de um jogo de RPG.
A seguir, faça outra função que recebe um dicionário contendo itens de RPG e a quantidade
dos mesmos e os adiciona em um inventário.
"""
def exibirInventario(mochila):
    #pass -> usa só para rodar quando não tem nada no escopo
    totalItens = 0
    #print(mochila.items())  items() é um método!
    for item, qtd in mochila.items():
        print(item + ": " + str(qtd))
        totalItens += qtd
    print("Total:" + str(totalItens))

def adicionarInventario(mochila, addItem):
    for item in addItem:
        mochila.setdefault(item, 0)
        mochila[item] += addItem[item]
    print(mochila)
    exibirInventario(mochila)
            

#MAIN
itens = {"corda": 2, "tocha": 6, "ouro": 42} #itens é um dicionário!
loot = {"ouro": 42, "corda": 4, "espada": 5}     # quando ganhar item, adiciona na mochila
exibirInventario(itens)
adicionarInventario(itens, loot)



    
