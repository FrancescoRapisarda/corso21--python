#mercoledi 25.10.2023
#LIST

#  sono collezioni di dati ORDINATE, INDICIZZATE, MODIFICABILI e permettono DUPLICATI

#  possiamo creare una lista con tipi uguali o eterogenei

#  vediamo: len(), type() e list()


    #  accediamo agli elementi della lista: singolo, range, negativo
    #  modificare elementi: singolo, range
    #  inserire elementi con append(), insert(), extend()
    #  rimuovere elementi con remove(), pop(), del(), clear()
    
        
        #  ciclare elementi: for in, per indice, while e short hand
        #  list comprehension
        #  modificare l'ordine: asc, desc, reverse
        #  copiare una lista con copy()
        #  unire piu liste insieme: +, append(), extend()

        
#LE LISTE SONO LE COLLEZIONI PIU FLESSIBILI CHE ABBIAMO IN PYTHON!


#  ES. LISTA:
x = ["milano","roma","napoli"]      #  tipi uguali
y = ["ciao", 34, True]              #  tipi eterogenei

print(type(x))
print(type(y))

print(len(x))
print(len(y))

z = list(("francesco", "davide", "federico"))   #  possiamo creare una lista tramite il costruttore list() ATTENZIONE: aggiungere () dentro il costruttore per inserire gli elementi.
print(type(z))



fruits = ["orange", "apple", "strawberry", "mango", "pere"]
print(fruits[0])    #accediamo agli elementi della lista: singolo

print(fruits[-1])   #accedo all'ultimo elemento della list

print(fruits[2:])   #range dall'indice 2 a tutto ciò che viene dopo

print(fruits[0:3])  #range dall'indice 0 all'indice 2 (escluso l'indice 3)

print(fruits[:4])   #range dall'indice 0 all'indice 3 (4 escluso)

print(fruits[-4:-2])   #range con indice negativo (andando a ritroso escluso -2) ['apple', 'strawberry']



#  modificare gli elementi

fruits[0] = "ananas"  #singolo
print(fruits)

fruits[1:3] = ["cocco", "ciliegia", "cocomero", "lampone"]  #range sostituisce elementi in fruits
print(fruits)


fruits[1:4] = ["avocado"]   #attraverso range sostituisco UNA sola volta "avocado" (non è un replace) come nuovo elemento della lista, nell'indice di partenza
print(fruits)


fruits.append("more")
print(fruits)               #append() aggiunge un elemento IN FONDO alla lista


fruits.insert(1,"limone")
print(fruits)               #insert() aggiunge un elemento facendo riferimento all'indice



cars = ["mercedes","fiat","peugeot","ferrari"]
cars2 = ["bmw","volvo","toyota"]

cars.extend(cars2)      #extend() facciamo fondamentalmente un append() con una lista che gia esiste
print(cars2)
print(cars)



cars.remove("peugeot")  #remove() rimuove l'elemento (non tramite indice!)
print(cars)


cars.pop()              #pop() rimuove l'elemento in coda
print(cars)


cars.pop(1)             #pop(1) posso rimuovere un elemento attraverso l'indice (possiamo dire che pop() è l'append della rimozione!)
print(cars)


del cars[0]             #del simile al pop()
print(cars)


#del cars                #in questo caso ci da problemi perchè x non esiste più perchè è stata rimossa run time!
print(cars)


cars.clear()               #clear() restituisce una lista pulita
print(cars)



#CICLARE GLI ELEMENTI DI UNA LISTA

dogs = ["Chico","Leo","Rocky"]

for dog in dogs:    #si legge cosi: "finchè (for) ci sono elementi in (in) dogs 
    print(dog)
    


#possiamo utilizzare gli indici:

dogs = ["Lilly","Chico","Leo","Rocky"]

for i in range(len(dogs)):
    print(dogs[i])




#possiamo usare anche il while per ciclare:

dogs = ["Pluto","Lilly","Chico","Leo","Rocky"]
i = 0
while i < len(dogs):
    print(dogs[i])
    i += 1


#short hand List Comprehension:
dogs = ["Snoopy","Pluto","Lilly","Chico","Leo","Rocky"]

[print(dog) for dog in dogs if dog != "Rocky"]       #ci permette di utilizzare una sintassi ridotta! [espressione for item in list if condizione == True]  (la condizione è facoltativa)


x = []

x = ["Beethoven" for dog in dogs if dog != "Leo"]  #sostituisci "Beethoven" in tutti gli indici di dogs e mettili nella lista x (se diverso da Leo allora gli indici saranno da 0 a 4)
print(x)





#ordinare una lista:

newspapers = ["La Sicilia", "Il Corriere della Sera", "Il Tempo","Il Fatto Quotidiano","Libero"]
newspapers.sort()       #ordinare la lista alfabeticamente
print(newspapers)

newspapers.sort(reverse=True)       #ordinare la lista alfabeticamente al contrario
print(newspapers)



#  La variabile di una lista funziona per RIFERIMENTO, ovvero fa riferimento all'allocazione di memoria della lista stessa
#Es.

lista1 = ["dentifricio","spazzolino", "shampoo","bagnoschiuma"]

lista2 = lista1        #lista2 contiene il RIFERIMENTO a lista1 (non è una copia indipendente!)

lista2[0] = "pettine"
print(lista1)
print(lista2)



#se volessi fare una copia distinta usare copy() in questo modo:

telephones = ["nokia","samsung","apple","xiaomi","sony"]
telephones2 = telephones.copy()
telephones2[0] = "honor"

print(telephones)
print(telephones2)



#oppure posso fare una copia con il costruttore list() in questo modo:

clothes = ["maglietta", "jeans","felpa","cappotto"]
clothes2 = list(clothes)

clothes2[2] = "maglione"

print(clothes)
print(clothes2)



# Unire più liste:

magazine = ["focus", "La Settimana Enigmistica", "Donna Moderna", "Giallo Zafferano"]
magazineTwo = ["Undici", "Internazionale", "DiPiu", "Chi", "Oggi"]

print(magazine + magazineTwo)

magazines = magazine + magazineTwo
print(magazines)


#oppure:
for rivista in magazineTwo:
    magazine.append(rivista)          #append() richiede ciclo for!
print(magazine)


#oppure:
magazinee = ["focus", "La Settimana Enigmistica", "Donna Moderna", "Giallo Zafferano"]
magazineTwoo = ["Undici", "Internazionale", "DiPiu", "Chi", "Oggi"]
magazinee.extend(magazineTwoo)
print(magazinee)



