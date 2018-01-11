#-*- coding: utf-8 -*-
from parsers.parsing import Parser
p=Parser("../../files/grafo.gr")
lista=p.get_list()
print(lista)