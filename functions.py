#venerdi 27.10.2023

# - FUNCTIONS

#  - Cosa sono le funzioni?
#  - Creare una funzione
#  - Chiamare una funzione

#  - Parametri in funzione
#  - Differenza tra argomenti e parametri
#  - Arbitrary Arguments, Keyword Arguments, Arbitrary Keyword Arguments (extra)
#  - Parametri di default
#  - Return dei valori 



def fai_la_pasta():             #creo funzione
    print("metti l'acqua")
    print("fai bollire")
    print("metti la pasta")
    
fai_la_pasta()                  #chiamo la funzione
fai_la_pasta()


def fai_la_pasta(tipo_pasta):           #parametro (variabile generica che utiliziamo nella funzione della variabile)
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    
fai_la_pasta("fusilli")                 #argomento (è il valore effettivo quando chiamiamo la funzione, in questo caso "fusilli")
fai_la_pasta("spaghetti")           




def fai_la_pasta(tipo_pasta, metti_il_sugo):       #piu parametri
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if metti_il_sugo:
        print("prepara sugo")
        
fai_la_pasta("maccheroni", True)


#  - Arbitrary Arguments, Keyword Arguments, Arbitrary Keyword Arguments (extra)

#Non sappiamo quanti argomenti (parametri) dobbiamo mettere?

def fai_la_pasta(*opzioni):       #metto tutti i parametri che voglio poi ci pensa python a gestirli (Arbitrary Arguments)
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + opzioni[0])
    if opzioni[1]:
        print("prepara sugo")
        
fai_la_pasta("fusilli", True)




def fai_la_pasta(tipo_pasta, sugo):    
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if sugo:
        print("prepara sugo")
        
fai_la_pasta(sugo=True, tipo_pasta="cannelloni")           #Keyword Arguments




#Arbitrary Keyword Arguments (extra) CERCARE SU INTERNET!!!





#Parametri di default:

def fai_la_pasta(tipo_pasta = "maltagliata", sugo = True):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)
    if sugo:
        print("sugo")
    
fai_la_pasta() 
fai_la_pasta("spaghetti")
fai_la_pasta("conchigliette",False)



#  - Return dei valori 

def sum(num1, num2):
    somma = num1 + num2
    return somma


x = sum(2,3)    

print(x)



