#giovedi 26 ottobre 2023
#SET

# - Collezioni di dati NON ORDINATE, NON INDICIZZATE, NON MODIFICABILI e non permettono duplicati
# - Creare una tupla normale e eterogenea
# - Vediamo len(), type() e set()

# - Accedere agli elementi con loop
# - Modificare elementi NON E' POSSIBILE, possiamo solo AGGIUNGERE e RIMUOVERE
# - Aggiungere elementi add(), update()
# - Rimuovere elementi con remove(), discard(), pop(), clear(), del
# - Unire con union() e update(), intersection_update(), intersection(), symmetric_difference_update(), symmetric_difference()


persons = {"Francesco", "Davide", "Federico", "Maria", "Maria"}     #non permette duplicati (Maria verrà preso solo una volta)!
personsTwo = {"Giuseppe", True, 18}
print(persons)
print(len(persons))
print(type(persons))

people = set(("Marco", "Luca", "Giovanni"))     #costruttore set()
print(people)
print(type(people))
print(len(people))


#  - accedere agli elementi con loop
for name in people:
    print(name)

print("Francesco" in people)    #faccio un check per vedere se "Francesco" è nel set "people" (restituisce un Booleano!) 
print("Luca" in people)     #True (esiste nel set!) 




#  - Aggiungere elementi al set:

x = {"Milano", "Napoli", "Genova"}
y = {"Catania", "Palermo", "Trapani"}
z = {"Como", "Firenze", "Imola"}


x.add("Roma")     #add() aggiunge un solo elemento al set
print(x)


#oppure update() che aggiunge piu elementi al set:

x.update(y)     #I VARIANTE
print(x)

z.update(["Siracusa","Caltanissetta","Foggia"])    #II VARIANTE
print(z)



# - Rimuovere elementi con remove(), discard(), pop(), clear(), del

x.remove("Napoli")       #I VARIANTE remove()
print(x)

x.discard("Milano")      #II VARIANTE discard() ATTENZIONE discard() si differenzia da remove() in quanto remove() ci darà problemi se tentiamo di rimuovere un elemento del set che non esiste (dovremmo in questo caso prevedere un modo per acchiappare l'errore ovvero il catch), mentre discard() dice: "l'elemento che volevo eliminare non esiste? Va beh ignoro il problema e vado avanti!"
print(x)


x.pop()        #toglie un elemento dal set (casuale) 
print(x)       


x.clear()       #pulisce il set


del x           #elimina il set (ci darà problemi perchè una volta eliminato non esiste piu)




# - Unire con union() e update(), intersection_update(), intersection(), symmetric_difference_update(), symmetric_difference()

a = {"Smartphone", "Laptop", "TV", "Tablet"}
b = {"Libro", "Scrivania", "Sedia", "Laptop"}

z = a.union(b)      #crea un NUOVO SET (esclude elementi duplicati)
print(z)

a.update(b)         #unisce e aggiorna il set esistente ma NON crea un nuovo set (esclude elementi duplicati)
print(a)



#se voglio lavorare con ELEMENTI DUPLICATI devo usare intersection() o intersection_update() che restituisce l'ELEMENTO DUPLICATO:
c = {"Smartphone", "Laptop", "TV", "Tablet"}
d = {"Libro", "Scrivania", "Sedia", "Laptop", "Smartphone"}

e = c.intersection(d)        #intersezione fra due set e crea un NUOVO SET con gli elementi DUPLICATI
print(e)

c.intersection_update(d)     #intersezione fra due set esistenti (restituisce elementi DUPLICATI)
print(c)




#se voglio prendere solo gli elementi NON DUPLICATI devo usare symmetric_difference_update() o symmetric_difference() :
f = {"Smartphone", "Laptop", "TV", "Tablet"}
g = {"Libro", "Scrivania", "Sedia", "Laptop", "Smartphone"}

h =f.symmetric_difference(g)
print(h)                             #differenza fra due set, crea un NUOVO SET escludendo elementi DUPLICATI

f.symmetric_difference_update(g)     #differenza fra due set esistenti (esclude elementi DUPLICATI)
print(f)





