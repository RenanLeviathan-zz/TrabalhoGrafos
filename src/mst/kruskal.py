#-*- coding:utf-8 -*-
'''
Created on 12 de nov de 2017

@author: Israël& Renan
'''
from plot import Plot
grafo=[
  ('0','2',5),
  ('0','3',8),
  ('1','2',16),
  ('1','4',30),
  ('1','6',26),
  ('2','3',10),
  ('2','4',3),
  ('3','4',2),
  ('3','5',18),
  ('4','5',12),
  ('4','6',14),
  ('5','6',4)
  ]
pos={
  '0':(50,100),
  '1':(200,50),
  '2':(100,50),
  '3':(100,150),
  '4':(150,100),
  '5':(200,150),
  '6':(250,100)
  }


parent=dict()
rank=dict()
#cria conjunto para verificação de acíclicos
def create_set(vertice):
    parent[vertice]=vertice
    rank[vertice]=0
    
def find(vertice):
    if parent[vertice]!=vertice:
        parent[vertice]=find(parent[vertice])
    return parent[vertice]   

def union(v,w):
    r1 =find(v)
    r2 = find(w)
    if r1 != r2:
        if rank[r1]>rank[r2]:
            parent[r2]=r1
        else:
            parent[r1]=r2
            if rank[r1]==rank[r2]:rank[r2]+=1
#ordena as arestas em ordem decrescente
global H
grafo.sort(key=lambda a : a[2])
H=grafo
global T
T=[]
global i
i=1
for v in pos.keys():
    create_set(v)
for h in H:
    v,w,p = h
    if find(v)!=find(w):
        union(v,w)
        T.append((v,w))
print(T)
g=Plot(T, pos)
g.plot("Arvore geradora mínima (Algoritmo de Kruskal)")