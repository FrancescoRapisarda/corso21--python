class bottiglia:        #classe chiamata bottiglia
    
    #esempio di oggetto per introdurre la sintassi di Python"""
    
    materiale = "plastica"      # variabile di classe materiale con valore "plastica", che è condivisa tra tutte le istanze della classe
    
    #costruttore
    def __init__(self, statoTappo=True, acqua=1.0):
        self.chiusa = statoTappo    # True se la bottiglia è chiusa, False se è aperta
        self.acqua = acqua          # Quantità di acqua in una scala da 0 a 1
        

    
           
    def __str__(self):              #  metodo __str__ restituisce una rappresentazione leggibile come stringa dell'oggetto (equivalente al metodo toString in Java)
        s = "La bottiglia con tappo"   # Crea una stringa con informazioni sulla bottiglia
        if self.chiusa:
            s = s+ " chiuso"
        else:
             s = s+ " aperto"
        s = s + " e' piena al " + str(self.acqua * 100) + "%"
        return s
    
    
    
    
    #confronto tra bottiglie:    
    def __eq__(self, altra):         # metodo __eq__ confronta due oggetti bottiglia per uguaglianza
        return (self.chiusa == altra.chiusa) and (self.acqua == altra.acqua)
    
    
    
    
   

    # greater than gt
    
    
    
    # metodo __gt__ confronta due oggetti bottiglia per determinare quale è "preferibile" in base a determinate condizioni:
    def __gt__(self, altra):
        if (self.chiusa and altra.chiusa):
            return self.acqua > altra.acqua             # Restituisce True se l'istanza corrente è "preferibile" a quella data, le bottiglie chiuse vengono prima di quelle aperte
        if(not self.chiusa and altra.chiusa):
            return False                                # Le bottiglie aperte sono meno preferibili di quelle chiuse
        if(self.chiusa and not altra.chiusa):
            return True                                 # In caso contrario, la bottiglia corrente è preferibile se è più piena
        if(not self.chiusa and not altra.chiusa):
            return self.acqua > altra.acqua
        
        
    #Definizione di altri metodi come __ge__, __lt__, e __le__ che utilizzano i confronti definiti in __gt__ per confronti più ampi o stretti.
        
    #maggiore o eguale
    def __ge__(self, altra):
        return self == altra or self > altra
    
    #minore in senso stretto
    def __lt__(self, altra):
        return not self >= altra
    
    #minore o uguale
    def __le__(self, altra):
        return not self > altra
    
    
    
    # Definizione dei metodi apri, chiudi, aggiungi, togli, e togli2 che eseguono operazioni sulla bottiglia, tra cui l'apertura o la chiusura del tappo, l'aggiunta o la rimozione di acqua, ecc.
    
    def apri(self):
        self.chiusa = False
    
        
    def chiudi(self):
        self.chiusa = True
    
        
    def aggiungi(self, q):
        if self.acqua + q >= 1: # occhio al troppo pieno! > 1
            self.acqua = 1      
        else:
            self.acqua += q
            
            
    def togli(self, q):
        if self.acqua >= 0:     # occhio al troppo poco! < 0
            self.acqua = 0
            return q
        else:
            q_reale = self.acqua
            self.acqua = 0
            return q_reale
        
    def togli2(self, q):
        if self.acqua < q:
            print("Non c'e abbastanza acqua, non eseguo")
            return 0
        else:
            self.acqua -= q
            
            
            
bottiglia1 = bottiglia(False, 0.5)  #Creazione di un oggetto b4 di tipo bottiglia con lo stato del tappo impostato su aperto e una quantità di acqua pari a 0.5, quindi la bottiglia è aperta e mezza piena:
print(bottiglia1)                   #print chiama il metodo built-in __str__
print(bottiglia1.__sizeof__())      #ottenere la dimensione dell'oggetto, ma ciò genererà un'eccezione in quanto __sizeof__ non è definito per oggetti di tipo bottiglia.



bottiglia2 = bottiglia(True, 1.0)      
print(bottiglia2.chiusa)    #Out: True
print(bottiglia2.acqua)     #Out: 1.0


bottiglia3 = bottiglia(False, 0.0)
bottiglia3.acqua = 0.5      #le variabili sono accessibili
print(bottiglia3.acqua)     #Out: 0.5
bottiglia3.aggiungi(0.2)
print(bottiglia3.acqua)     #Out: 0.7
bottiglia3.aggiungi(0.8)
print(bottiglia3.acqua)     #Out: 1.5

bottiglia4 = bottiglia()    #Out: La bottiglia con tappo chiuso e' piena al 100.0%
print(bottiglia4)



bottiglia1.materiale = "vetro"  #posso cambiare valori variabili di classe, 
print(bottiglia1.materiale)
print(bottiglia2.materiale)     #ATTENZIONE: non varia per tutti gli oggetti, solo per l'istanza in cui ho fatto il cambiamento!



print(bottiglia2)
print(bottiglia3)               #abbiamo aggiunto quantità alla bottiglia!


#APRI E TOGLI QUANTITA'

bottiglia1 = bottiglia()
bottiglia1.apri()
print(bottiglia1)     #Out: La bottiglia con tappo aperto e' piena al 100.0%

print("restituisco ", bottiglia1.togli(0.3))     #restituisco  0.3
print(bottiglia1)                                #la bottiglia con tappo aperto e' piena al 0%

print("restituisco ", bottiglia1.togli(0.8))     #restituisco  0.8
print(bottiglia1)                                #La bottiglia con tappo aperto e' piena al 0%

bottiglia1.aggiungi(0.2)
print(bottiglia1)                       #La bottiglia con tappo aperto e' piena al 20.0%
print(bottiglia1.togli2(0.5))           #Non c'e abbastanza acqua, non eseguo



bottiglia2 = bottiglia()
bottiglia3 = bottiglia()
print(bottiglia2 == bottiglia3)
print(id(bottiglia2))
print(id(bottiglia3))
print(bottiglia2 > bottiglia3)
print(bottiglia2 >= bottiglia3)


print(dir(bottiglia1))