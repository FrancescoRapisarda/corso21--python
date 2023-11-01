#   25/10/2023
#   Introduzione a collezioni di dati
#   - list, tuple, set, dictionary


#   spiegazione termini:

    #   - ordinato: la collezione ha ordine ben definito e l'aggiunta di elementi non incide
    #   - indicizzato: possiamo accedere agli elementi tramite indice (index)
    #   - modificabile: possiamo aggiungere, cambiare e rimuovere elementi una volta creata la collezione
    #   - immutabile: non possiamo aggiungere, cambiare e rimuovere elementi
    #   - permette duplicati: possono esserci più elementi con lo stesso valore

#  Le LISTE sono collezioni ORDINATE e MODIFICABILI. Permettono duplicati.
#  Le TUPLE sono collezioni ORDINATE ma IMMUTABILI. Permettono duplicati.
#  I SET sono collezioni NON ORDINATE e perciò NON INDICIZZATE. Non permettono duplicati.
#  I DICTIONARY sono collezioni ORDINATE* e MODIFICABILI (dalla versione 3.7). Non permettono duplicati.


#  Una variabile è diversa da una collezione di dati, poichè una variabile avrà assegnato un solo valore.
 
#  Una collezione può racchiudere più valori (racchiuse in delle parentesi) anche se fanno capo ad un unica variabile.


#  OGNI COLLEZIONE (list, tuple, set e dictionary) HA DELLE PROPRIETA' DIVERSE, 
#  non è solo la parentesi a cambiare o la conformazione sintatica di queste collezioni di dati. 




#   Esempio LISTE:
citta = ["Palermo", "Catania", "Siracusa", "Ragusa", "Caltanissetta"]
print(citta[0])  # Palermo avrà sempre indice 0, Catania avrà sempre indice 1, Siracusa avrà sempre indice 2 e cosi via.. [collezione ORDINATA, MODIFICABILE e INDICIZZATA (possibile accedere tramite un indice)]

citta = ["Trapani","Palermo", "Catania", "Siracusa", "Ragusa", "Caltanissetta"]     #  collezione MODIFICABILE
print(citta[0])

citta = ["Trapani","Palermo", "Catania", "Siracusa", "Ragusa", "Trapani"]     #  permette duplicati
print(citta)



#  Esempio TUPLE:
persone = ("Francesco", "Davide", "Federico", "Riccardo", "Giuseppe")
print(persone[0])       #[collezione ORDINATA, dunque INDICIZZATA (possibile accedere tramite un indice)]

persone = ("Francesco", "Davide", "Federico", "Riccardo", "Francesco")  #collezione IMMUTABILE, una volta creata la tupla non posso più aggiungere elementi!
print(persone)       #permette duplicati



#  Esempio SET:
fruits = {"apple", "banana", "ananas", "ananas"} #collezione NON ORDINATA (elementi disposti randomicamente), non INDICIZZATA (gli elementi non hanno indice e non è possibile accedervi tramite esso).
print(fruits)       #non ammette duplicati. I SET SONO LE COLLEZIONI PIU' RIGIDE IN ASSOLUTO!


fruits.add("orange")    # add un elemento al set
print(fruits)           # print il set dopo l'aggiunta


fruits.remove("banana") # remove un elemento dal set
print(fruits)           # print il set dopo la rimozione


print("apple" in fruits)  # True   # Verifica se un elemento è presente nel set (restituisce un BOOLEANO)
print("grape" in fruits)  # False  # Verifica se un elemento è presente nel set (restituisce un BOOLEANO)


for fruit in fruits:      # Itero attraverso gli elementi del set
    print(fruit)

print(len(fruits))       # length del set



#  Esempio DICTIONARY:
person = {                  #  Collezioni ORDINATE* (dalla versione 3.7) e MODIFICABILI . 
    "name": "John",
    "age": 30,
    "city": "New York",
    "city": "New York"      #  Non permettono duplicati!
}

print(person)


# Accesso ai valori del dizionario
print(person["name"])  # Stampa "John"
print(person["age"])   # Stampa 30


# Modifica dei valori del dizionario
person["age"] = 31
print(person["age"])   # Stampa 31
print(person)


# Aggiunta di nuove coppie chiave-valore
person["job"] = "Engineer"
print(person)


# Rimozione di una coppia chiave-valore
del person["city"]
print(person)


# Verifica se una chiave è presente nel dizionario
print("name" in person)  # True (restituisce un BOOLEANO)
print("city" in person)  # False (restituisce un BOOLEANO)


# Iterazione attraverso le chiavi del dizionario        I ALTERNATIVA
for key in person:
    print(key, ":", person[key])
    

# Iterazione attraverso le coppie chiave-valore         II ALTERNATIVA
for key, value in person.items():
    print(key, ":", value)

