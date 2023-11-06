# -*- coding: utf-8 -*-

"""
Created on Mon Oct 23 08:46:34 2023
"""



#file

# Funzione fondamentale per i file è open()


# Creazione di un file di testo:

# come primo parametro bisogna mettere una stringa contenente il "nome del file";

# come secondo parametro si dà "la funzione" da eseguire;


# modalità x (crea un file SE non esiste)
myFile = open("fileOne.txt","x")    #Apri un file chiamato "fileOne.txt" in modalità "x". La modalità "x" viene utilizzata per aprire un file in modalità di scrittura esclusiva, il che significa che il file verrà creato SE non esiste e se esiste già, verrà sollevata un'eccezione. 

print(type(myFile))    # myFile è un oggetto di tipo TextIOWrapper
print(dir(myFile))     # stampa l'elenco dei metodi disponibili per l'oggetto myFile


# scriviamo qualcosa:
myFile.write("Francesco")  # scrive la stringa "Francesco" nel file aperto. Se il file non esiste, verrà creato. La stringa sarà scritta senza un carattere di nuova riga, quindi se volessi scrivere "Francesco" e "Rapisarda" su righe separate, dovrei aggiungere "\n" alla fine della prima scrittura.
myFile.write("Rapisarda")  # scrive la stringa "Rapisarda" nella stessa riga in cui è stata scritta "Francesco"


# è veramente scritto sul mio disco?
myFile.close()          # questa istruzione CHIUDE il file myFile. È importante chiudere il file dopo aver finito di scriverci o leggerci per rilasciare le risorse del sistema.



myFile = open("fileTwo.txt","r")     # apro un nuovo file chiamato "file02.txt" in modalità di lettura ("r"). Questo mi permette di LEGGERE il contenuto del file.

s = myFile.read()                   # questa istruzione legge l'intero contenuto del file aperto ( attraverso metodo read() ) e lo assegna alla variabile s. Il contenuto del file sarà memorizzato nella stringa s.
print(s)

myFile.close()                      # chiude il file myFile precedentemente aperto in modalità di lettura.


# Ho aperto, scritto e letto da due file diversi. Posso esaminare il contenuto del file "file02.txt" nella variabile s.



# Anche i file sono iterable:
myFile = open("fileTwo.txt","r")
s = myFile.read()

for item in s:
    print(item)
    
myFile.close()



# altro esempio:
myFile = open("numbers.txt", "w")   # Apro un file chiamato "numbers.txt" in modalità di scrittura


for i in range(1, 6):               # Utilizzo un ciclo for per scrivere numeri da 1 a 5 nel file (6 escluso)
    myFile.write(str(i) + "\n")     # Scrivo il numero seguito da un carattere di nuova riga

myFile.close()      # Chiudo il file



# creo e apro il file "fileThree":
#myFile = open("fileThree.txt", "x")    # se il file esiste verrà sollevata un eccezione (modalità x - modalità di scrittura esclusiva)

#myFile.close()




#apro il file per SCRIVERE e ci scrivo qualcosa:
myFile = open("fileThree.txt","w")

for number in range(100):   # range da 0 a 99 (100 escluso)

    myFile.write(str(number) + "\n")      

myFile.close()





# apro di nuovo per leggere:
myFile = open("fileThree.txt","r")

for number in myFile:

    print(number)

myFile.close()



# apro file (se esiste se non esiste lo crea) in scrittura e ci scrivo dentro qualcosa:
myFile = open("fileFive.txt", "w")

s = "Nel mezzo del cammin di nostra vita"  #definisco una stringa con la medesima frase
L = s.split()                              #split di default mi separa le parole con uno spazio

for word in L:
    myFile.write(word + "\n")
myFile.close()



#leggo il file:
myFile = open("fileFive.txt", "r")

for word in myFile:
    print(word)
myFile.close()



# CREARE UN FILE BINARIO:
myFile = open("fileSix.txt", "wb")  # Utilizzo "wb" per la scrittura binaria

s="abcdefghilmnopqrstuvz"

for i in range (10):
    myFile.write(bytes([i]))        # converto il valore intero in un byte e lo scrivo nel file

myFile.close()


# LEGGERE IL FILE BINARIO:
myFile = open("fileSix.txt", "rb")   # riapro lo stesso file in modalità di lettura binaria

content = myFile.read()              # leggo il contenuto del file

for item in content:
    print(item)
    
myFile.close()


# Decodifico il contenuto in una stringa
decoded_content = "".join(chr(byte) for byte in content)
print(decoded_content)
