#giovedi 26.10.2023
#TUPLE

#  sono collezioni di dati ORDINATE, INDICIZZATE, NON MODIFICABILI e permettono DUPLICATI

#  possiamo creare una tupla normale e con un valore, singola e eterogenea

#  vediamo: len(), type() e tuple()


    #  accediamo agli elementi della tupla: singolo, range, negativo
    #  verificare se elemento esiste
    #  modificare elementi: NON POSSIBILE (se non con escamotage)
    #  inserire elementi con append(), insert(), extend()
    #  rimuovere elementi (con escamotage) oppure cancellare tutto con del()
    #  spacchettare una tupla (unpack) normale e con *
    #  ciclare elementi
    #  unire tuple con join()
    #  metodi count() e index()
    

x = ("milano","roma","napoli")      #una tupla deve avere almeno due elementi separati da virgola altrimenti se dentro le parentesi abbiamo ad esempio "milano" sarà di tipo string e non tuple!
y = tuple(("milano",True,45))       #un'altra possibile alternativa alla creazione di una tupla
z = ("Siracusa",)                   #aggiungere una virgola per avere una tupla con UN SINGOLO valore

print(type(x))  #tipo
print(type(z))  #tipo
print(len(x))   #lunghezza della tupla

print(type(y))
print(len(y))

print(x[0])
print(x[0:2])   #possiamo accedere esattamente come le liste



#VERIFICARE se elemento esiste:

if "milano" in x:       #possiamo fare la seguente verifica anche sulle liste
    print("ok")



#MODIFICARE gli elementi di una tupla non è possibile (ma c'è un'escamotage):

x = ("milano","roma","napoli")
y = list(x)     #passaggio per copia (trasforma una tupla in una list)
print(x)
print(y)

y[1] = "Catania"
print(y)

x = tuple(y)
print(x)


#Rimuovere elementi (con escamotage già vista):
y.remove("napoli")
print(y)

x = tuple(y)
print(x)


#oppure con del (ATTENZIONE del elimina tutta la tupla e ci darà errore in fase di esecuzione del codice)
#del x
print(x)



#Spacchettare una tupla:

citta = ("genova", "catania", "palermo")
(x, y, z) = citta     #spacchettare una tupla (unpack) normale
print(x)    #  genova
print(y)    #  catania
print(z)    #  palermo


#oppure:
cittaa = ("genova", "catania", "palermo", "venezia")
(x, y, *z) = cittaa     #spacchettare una tupla (unpack) con *
print(x)    #  genova
print(y)    #  catania
print(z)    #  ['palermo', 'venezia']



#ciclare elementi di una tupla:
for city in citta:
    print(city) 


#oppure:
for i in range(len(citta)):
    print(citta[i])
    

#oppure:

i = 0
while(i < len(citta)):
    print(citta[i])
    i += 1
    
    
    
#Unire le tuple:

lista_citta = ("genova", "catania", "palermo", "venezia")
lista_citta_2 = ("firenze", "roma", "cagliari")

y = lista_citta + lista_citta_2
print(y)



#oppure concatenare stringhe di caratteri:
z = ", "

result = z.join(lista_citta)
print(result)



#metodi count() e index():
animals = ("giraffa", "elefante", "mucca", "leone", "giraffa")
print(animals.count("giraffa"))     #Out: 2 (elementi ripetuti)
print(animals.index("giraffa"))       #Out: 0 (indice dell'elemento nella tupla. ATTENZIONE prende prima occorrenza!)
