# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:45:22 2023

@author: franc
"""

#strutture built-in "predefinite" di Python

#lista
#tupla

L=[1,2,3] #lista
T=(1,2,3) #3-tupla tripla o 3-upla è un oggetto che contiene una serie di numeri che non vogliamo cambiare

L[0]=11
T[0]=11 #genera un errore le tuple sono IMMUTABILI, ma possono contenere come tutte le liste valori eterogenee

print(len(L))
print(len(T))

print("Lista L tipo", type(L), "numero metodi", len(dir(L)))
print("Lista T tipo", type(T), "numero metodi", len(dir(T)))

T_problema=(1,[1,2,3])
len(T_problema)
print(T_problema[1])
T_problema [1][0]=10


#insiemi in Python
S={0,1,2,3,4,11,7,"ciao",True, True, False}  #un elemento non puo essere ripetuto!
print(S)
print(type(S))
print(len(S))

squadre={"Catania","Inter","Juve","Milan","Milan"} 
print(squadre)

T2=(1,2,3)
for i in T2:
    print(i)
    
    
    
for s in squadre:
    print(s)
    
    dir(squadre)
    
    #alcuni metodi dei set
    
    squadre.add("Roma")
    print(squadre) #gli insiemi non sono ordinati!
    
    
    teams = squadre #abbiamo dato un ulteriore riferimento o nome al set "squadre" non abbiamo creato unaltra copia
    print(teams)
    teams.add("Lazio")
    print(teams)
    print(squadre)
    
    
    teams.clear()
    print(teams)
    print(squadre)
    
    
    #insiemi piu veloci da scrivere
    A={} #questo crea un dizionario
    A1=set() #insieme vuoto (set)
    B={1,2,3,4,5,6}
    C={2,4,6}
    D={1,3,5}
    E={3,4}
    
    print(type(A))
    print(type(A1))
     
    
    #operazioni insiemistiche
    
    
    #differenza
    F=B.difference(C)
    print(F)
    
    #unione
    G=B.union(C)
    print(G)
    
    
    #intersezione
    H= B.intersection(D)
    print(H)
    
    B.pop()
    print(B)
    
    print(B.remove(5))
    print(B)
    
    
    print(C.isdisjoint(D))
    
    print(C.issubset(D))
    
    print(C.issuperset(D))