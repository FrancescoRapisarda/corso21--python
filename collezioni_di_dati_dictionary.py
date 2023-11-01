#venerdi 27 ottobre 2023

#  - Collezioni di dati ordinate, modificabili ma non permettono duplicati (chiave)
#  - Creare un dict
#  - Vediamo len(), type()

#  - Accedere agli elementi con [], get(). keys(), values(). items(), controllare se chiave esiste
#  - Modificare elementi con [] e update()
#  - Aggiungere elementi con [] e update()
#  - Rimuovere elementi con pop(key), popitem(), clear(), del
#  - Ciclare elementi: key, values, values(), keys(), items()
#  - Copiare dict con copy() e dict()
#  - Dict annidati



#Creo un dictionary ovvero l'equivalente degli oggetti in Javascript (molto descrittivo):
person = {
    "name" : "Francesco",       #coppia chiave - valore (NON è possibile avere una chiave DUPLICATA!)
    "surname" : "Rapisarda",
    "age" : 34,
    "address" : {                       #dict annidati
        "address" : "Via Tivoli",
        "number" : 2,
        "cap" : 95024,
        "city" : "Acireale"
    },
    "hobby" : ["Photography", "Novel", "Development"]  #list annidate
}

print(person)
print(len(person))
print(type(person))     #dict



#come prendere un valore dentro un dict ANNIDATO?
print(person["address"]["cap"])     #non possiamo prendere piu chiavi per mostrare i loro valori!


#prove personali sui dict annidati:
a = person["address"]["cap"]            #95024
b = person["address"]["city"]           #Acireale
print("cap: " + str(a)+ ", citta': " + b)


#  - Accedere agli elementi con [], get(). keys(), values(). items(), controllare se chiave esiste

print(person["surname"])    #accedo tramite CHIAVE!               I VARIANTE

print(person.get("name"))   #accedo tramite CHIAVE! con get()     II VARIANTE


print(person.keys())    #restituisce una lista con dentro le chiavi dell'oggetto "person"

#stessa cosa, assegniamo person alla variabile x e ci restituisce le chiavi dell'oggetto attraverso il costruttore keys():
x = person.keys()
print(x)
print(type(x))

x = person.values()     #restituisce una lista con dentro i valori delle chiavi dell'oggetto "person" (ATTENZIONE: stampa chiavi DI CHIAVI e i loro rispettivi valori!)
print(x)


x = person.items()      #ci restituisce una lista di tuple, dove ogni tupla rappresenta chiave-valore dell'oggetto
print(x)


print("name" in person)  #"la chiave esiste?"  TRUE (restituisce un Booleano!)
print("second_name" in person)   #FALSE




#  - Modificare elementi con [] e update()

person["name"] = "Davide"       #[]
print(person)


person.update({"name" : "Federico"})    #update()
print(person)




#  - Aggiungere elementi con [] e update()

person["codice fiscale"] = "RPSFNC89M02A028F"   #[]    (ATTENZIONE chiave-valore aggiunti in coda!)
print(person)


person.update({"friends" : ["Federico", "Simone"]}) #update()  (ATTENZIONE chiave-valore aggiunti in coda!)
print(person)




#  - Rimuovere elementi con pop(key), popitem(), clear(), del

person.pop("name")  #pop(key)
print(person)


person.popitem()    #popitem() rimuove l'ultimo item in coda!
print(person)


person.clear()      #clear() pulisce il dict
print(person)


#del person          # del nome_dict elimina definitivamente il dict (ci darà errore in print perchè non esiste più!)
#print(person)




#  - Ciclare elementi: keys, values, values(), keys(), items()

person = {
    "name" : "Francesco",       #coppia chiave - valore (NON è possibile avere una chiave DUPLICATA!)
    "surname" : "Rapisarda",
    "age" : 34,
}

for key in person :     #mostrami le chiavi (keys)
    print(key)

#oppure:

for key in person.keys() :    #mostrami le chiavi ( tramite costruttore keys() )
    print(key)
    

for key in person :     #mostrami i valori (values)
    print(person[key])                    

#oppure:

for key in person.values() :    #mostrami i valori ( costruttore values() )
    print(key)



for key, value in person.items() :  #mostrami key e value (costruttore items() )
    print(key, value)
    
    

    
#  - Copiare dict con copy() e dict()

person = {
    "name" : "Francesco",       #coppia chiave - valore (NON è possibile avere una chiave DUPLICATA!)
    "surname" : "Rapisarda",
    "age" : 34,
}

# x = person   ATTENZIONE: in questo caso avrei una reference (ovvero x (un puntatore) che punta all'indirizzo di memoria di person!)

x = person.copy()       # COPIA del dict (x è una variabile distinta se modifico x non modifico person, proprio perchè è una COPIA!)
print(x)
print(type(x))          # dict


#altrimenti uso il costruttore dict() :
x = dict(person)        #crea una COPIA del dict nella variabile x; varibile x conterrà un dict nuovo e indipendente da person!
print(x)

