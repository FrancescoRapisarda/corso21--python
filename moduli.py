#domenica 29.10.2023
# - Moduli

#   - cos'è un modulo
#   - creare un modulo
#   - funzioni e variabili in un modulo
#   - creare un alias
#   - moduli built in (platform, math)
#   - funzione dir()
#   - importare solo una parte del modulo




"""Un "modulo" è un file che contiene definizioni di funzioni, variabili e istruzioni 
che possono essere riutilizzate in altri programmi. 
Questi moduli sono utilizzati per organizzare il codice in unità logiche e riutilizzabili, 
rendendo più semplice la gestione e la manutenzione del codice.
I moduli possono contenere funzioni, classi, variabili globali e istruzioni, 
e possono essere importati in altri programmi Python per accedere 
alle definizioni contenute al loro interno. 
Per importare un modulo in un programma Python, si utilizza l'istruzione import. 
Ad esempio, se si ha un modulo chiamato "mio_modulo.py" che contiene alcune funzioni, 
è possibile importare questo modulo in un altro file Python.
"""


def saluta(nome):
    print("ciao " + nome)
    
    
persona1 = {
    "nome" : "Francesco",
    "cognome" : "Rossi",
    "eta" : 25
}