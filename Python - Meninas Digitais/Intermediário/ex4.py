# -*- coding: cp1252 -*-
"""
4) Crie um programa que seja uma extensão do “estou com sorte” do Google: digite uma string
que será procurada na busca do Google e, a seguir, abra no seu navegador em 5 abas
diferentes os 5 primeiros lugares que aparecem no ranking da busca.
"""
import requests, bs4, webbrowser, sys, time
#print(sys.argv)
termos = sys.argv[1]
res = requests.get("https://www.google.com/search?q="+termos)
#print(res)          -> 200 = conexão ok
res.raise_for_status()  #trata exceção de erro na conexão
print(res.text) #printa o codigo html
bso = bs4.BeautifulSoup(res.text,"lxml")
linkEles = bso.select('a')    # CSS: pega o conteudo da classe r com o elemento a
numOpen = min(5, len(linkEles))
for i in range(numOpen):
    webbrowser.open("https://google.com"+linkEles[i].get('href'))
print(numOpen)


#from pprint import pprint
#pprint(vars(linkEles))
