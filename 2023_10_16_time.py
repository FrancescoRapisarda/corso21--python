# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:05:49 2023

@author: franc
"""



"""
il computer lancia 3 dadi e fa un punteggio totale che viene
calcolato e stampato

IL GIOCATORE lancia 3 dadi e vede i punteggi realizzati

Il GIOCATORE puo decidere se e quali dadi vuole lanciare la senconda volta per cambare punteggio

dopo il secondo lancio del giocatore si calcola il punteggio definitivo del giocatore

vince chi fa il punteggio piu alto
a parità di punteggio vince il giocatore
"""

from random import randint

def lancio():
    return randint(1,6)



computer={"dado1":lancio(), 
          "dado2":lancio(),
          "dado3":lancio()
          }


giocatore={"dado1":lancio(), 
          "dado2":lancio(),
          "dado3":lancio()
          }


def punteggio(giocatore):
    """
    tot=0
    for i in giocatore:
        tot+=giocatore[i]
    return tot
    """
    return sum(giocatore.values())


print("COMPUTER")
print("dado1", computer["dado1"],
      "dado2", computer["dado2"],
      "dado3", computer["dado3"],
      )
print("Il computer totalizza: ", punteggio(computer))


print("GIOCATORE")
print("dado1", giocatore["dado1"],
      "dado2", giocatore["dado2"],
      "dado3", giocatore["dado3"],
      )
print("Il giocatore totalizza: ", punteggio(giocatore))



scelta=input("vuoi cambiare dado 1 (s/n)?")
if scelta=="s":
    giocatore["dado1"]= lancio()
    
scelta=input("vuoi cambiare dado 2 (s/n)?")
if scelta=="s":
    giocatore["dado2"]= lancio()
    
scelta=input("vuoi cambiare dado 1 (s/n)?")
if scelta=="s":
    giocatore["dado3"]= lancio()


if punteggio(giocatore)>=punteggio(computer):
    print("HAI VINTO!")
    print("PUNTEGGIO GIOCATORE: ", punteggio(giocatore), " ", "PUNTEGGIO COMPUTER: ", punteggio(computer))
else:
    print("HAI PERSO!")
    print("PUNTEGGIO GIOCATORE: ", punteggio(giocatore), " ", "PUNTEGGIO COMPUTER: ", punteggio(computer))




"""




DATE




"""

import time

from time import time
print(time())


inizio= time()
L=[i for i in range(10*10)] #list comprehension best!
fine=time()
print(fine-inizio)




inizio= time()
L=[]
for i in range(10**5): #for esplicito piu lento!
    L.append(i)
fine=time()
print(fine-inizio)





inizio= time()
totale=sum(L)   #sum è eseguito piu velocemente nella macchina!
fine=time()
print(fine-inizio)


inizio= time()
totale=0
for i in L:
    totale +=i  #ciclo for meno ottimizzato!
fine=time()
print(fine-inizio)





