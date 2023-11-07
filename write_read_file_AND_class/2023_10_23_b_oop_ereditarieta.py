#OOP ed ereditaretà

#creo un personaggio per un gioco RPG

class personaggio:
    #classe di generico personaggio per un gioco role play
    
    def __init__(self, nome, vita):
        self.nome = nome
        self.pv = vita
        
        
    def __str__(self):
        return "{} ha punti vita pari a {}".format(self.nome, self.pv)   #self.nome + " ha punti vita pari a "+ str(self.pv)


    def scontro(self, altro):
        pass
    
    
#collaudo
A = personaggio("Ken", 100)
print(A)


class potenzialita(personaggio):    #la classe eredita tutto quello che ha personaggio (specializzazione della classe personaggio)
    
    def __init__(self, nome, vita, potere):
        """
        potrei ricopiare quanto scritto nell-init della super classe personaggio:
        self.nome = nome
        self.pv = vita
        ma sono piu furbo..
        """
        super().__init__(nome, vita)
        self.pm = potere
        
    
    def __str__(self):
        return super().__str__() + " ha punti potere pari a " + str(self.pm)

    
    def scontro(self, altro):
        if isinstance(altro, potenzialita):
            if(self.pm >= altro.pm):
                altro.pv = altro.pv - (self.pm - altro.pm)
            else:
                self.pv = self.pv - (altro.pm - self.pm)
        
        if isinstance(altro, potenzialita): #lotta con guerriero
            if(self.pm >= altro.pa):
                altro.pv = altro.pv - (self.pm - altro.pa)
            else:
                self.pv = self.pv - (altro.pa - self.pm)
            
        

a = potenzialita("Daddy", 100, 100)
print(a)
b = potenzialita("Monkey", 200, 90)
print(b)
c = potenzialita("Orlando", 100, 90)
print(c)
print()
print()
#print(type(a))
print()
print()
print(isinstance(a, potenzialita))
print(isinstance(4.1, int))

# scontro A vs B
a.scontro(b)
print(a)
print(b)
print(c)
print()
    