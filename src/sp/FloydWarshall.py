#-*- coding: utf-8 -*-
'''
Created on 9 de dez de 2017

@author: Israël & Renan
'''
from parsers.parsing import *
class FW:
    def __init__(self,graph):
        self.G=graph
        self.mtx={}
        self.p={}
        
    def create_matrix(self):
        for u in self.G:
            self.mtx[u]={}
            for v in self.G:
                self.mtx[u][v]=10000
                
        for u in self.mtx:
            self.mtx[u][u]=0
            for v in self.mtx:
                if u==v:
                    self.mtx[u][v]=0
                else:
                    if v in self.G[u]:
                        self.mtx[u][v]=self.G[u][v]
    
    def begin(self):
        self.create_matrix()
        for k in self.G.keys():
            for v in self.G.keys():
                for w in self.G.keys():
                    if self.mtx[v][k]+self.mtx[k][w]<self.mtx[v][w]:
                        self.mtx[v][w]=self.mtx[v][k]+self.mtx[k][w]
                        self.p[v]=k
    
    def show_matrix(self):
        print("  ",end="")
        [print("| {}".format(u),end="") for u in self.G.keys()]
        print("|")
        for u in self.mtx:
            print("{} ".format(u),end="")
            for v in self.mtx[u]:
                print("| {}".format(self.mtx[u][v]),end="")
            print("")
                
filename=input("Arquivo do grafo:")
p=Parser(filename)
g=p.get_list()
fw=FW(g)
fw.begin()
fw.show_matrix()