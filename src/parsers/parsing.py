'''
Created on 25 de nov de 2017

@author: Renan
'''
class Parser:
    def __init__(self,filename):
        if filename[len(filename)-3:]=='.gr':
            self.file=open(filename,'r')
        else:
            self.file=None

    def automata(self,n,st):
        idx=''
        sidx=''
        q='q0'
        t=''
        for s in st:#para cada letra na string
            if q=='q0':
                if '0'<=s<='9':
                    q='q1'
                    idx=s
            elif q=='q1':
                if s==':':
                    q='q2'
                    n[idx]={}
                elif s=='>':
                    q='q3'
                elif '0'<=s<='9':
                    idx+s
                    if sidx!='':
                        sidx+=s
            elif q=='q2':
                q='q1'
                sidx=s
                n[idx][sidx]={}
            elif q=='q3':
                if s.isdigit():
                    t+=s
                    q='q4'
            elif q=='q4':
                if s.isdigit() or s==".":
                    t+=s
                if s==';':
                    q='q6'
                    n[idx][sidx]=float(t)
                    t=''
                if s==',':
                    q='q5'
                    n[idx][sidx]=float(t)
                    t=''
            elif q=='q5':
                sidx=s
                q='q1'
        return q=='q6'
    
    def get_list(self):
        lista={}
        for f in self.file:
            self.automata(lista, f)
        return lista