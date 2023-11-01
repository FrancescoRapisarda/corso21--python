# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:36:25 2023

@author: franc
"""

#dizionario

D={"presidente":"Beatrice",    #coppia chiave:valore (un ITEM ovvero coppia chiave valore)
   "vice":"Claudia",
   "tesoriere":"Erika",
   "segretario":"Desiree",
   "socio":"Alice"
   }

print(D["presidente"])
print(D["socio5"])

try:
    print(D["socio5"])
except KeyError:
    print("chiave inesistente!")
finally:
    print("la vita continua..")
    
    
#l'iterazione avviene sulle chiavi
for key in D:
    print(key)
    
    
#l'iterazione avviene sui valori    
for key in D:
    print(D[key])
    

#l'iterazione prende la chiave e il valore
for key in D:
    print(key,":", D[key])
    
print(D.keys()) #stampa tutte le chiavi
print(D.values()) #stampa tutti i valori
print(len(D))


#aggiungere un elemento ad un dizionario
D["socio2"]="Filippa"
print(D)

D[2]="Giulia"
print(D)


D.items() #restituisce delle tuple chiave valore


D.get("presidente") #restituisce il valore della chiave



E={"segretario":"Filippa","socio1":"Giulia","socio3":"Katia"}
D.update(E)

print(D)


D.pop("segretario")  #rimuove l'elemento
print(D)


D.popitem()  #ultimo elemento rimosso


