class Personaggio:      # class Personaggio
    
    def __init__(self, nome, livello, punti_salute):    # costruttore
        self.nome = nome
        self.livello = livello
        self.punti_salute = punti_salute


    def attacca(self, bersaglio):    # metodo attacca()
        danno = self.livello * 10    # calcolo il danno dell'attacco in base al livello del personaggio
        print(f"{self.nome} attacca {bersaglio.nome} e infligge {danno} punti di danno.")       # f sta per "formatted string". Questo tipo di stringa permette di inserire valori di variabili all'interno di una stringa in modo molto leggibile.
        bersaglio.subisci_danno(danno)
        


    def subisci_danno(self, danno):     # metodo subisci_danno()
        self.punti_salute -= danno      # Sottraggo i punti ferita subiti dal personaggio
        if self.punti_salute <= 0:
            print(f"{self.nome} e'stato sconfitto!")
        else:
            print(f"A {self.nome} gli rimangono {self.punti_salute} punti!")




class PersonaggioSpecifico(Personaggio):
    def __init__(self, nome, livello, punti_salute, arma, abilita_speciale):
        super().__init__(nome, livello, punti_salute)   # Chiamo il costruttore della superclasse
        self.arma = arma    # Aggiungo attributo specifico alla sottoclasse
        self.abilita_speciale = abilita_speciale    # Aggiungo attributo specifico alla sottoclasse

    def usa_abilita_speciale(self):
        print(f"{self.nome} utilizza l'abilita' speciale: {self.abilita_speciale}")     # Implemento un metodo specifico per l'abilità speciale




personaggio1 = PersonaggioSpecifico("Aragorn", 15, 150, "Spada di Anduril", "Risolutezza")
personaggio2 = PersonaggioSpecifico("Legolas", 8, 200, "Bastone allungabile", "Velocita")
personaggio3 = PersonaggioSpecifico("Federik", 2, 290, "Pc", "Logica")
personaggio4 = PersonaggioSpecifico("Gianko", 12, 400, "Manganello", "Caparbieta'")



print(f"{personaggio1.nome} di livello {personaggio1.livello}.")
print(f"Usa {personaggio1.arma} come arma principale.")
print("vs")
print(f"{personaggio2.nome} di livello {personaggio2.livello}.")
print(f"Usa {personaggio2.arma} come arma principale.")

print()
print()

print(f"{personaggio3.nome} di livello {personaggio3.livello}.")
print(f"Usa {personaggio3.arma} come arma principale.")
print("vs")
print(f"{personaggio4.nome} di livello {personaggio4.livello}.")
print(f"Usa {personaggio4.arma} come arma principale.")
print()



print(f"{personaggio1.nome} ha {personaggio1.punti_salute} punti salute.")
print(f"{personaggio2.nome} ha {personaggio2.punti_salute} punti salute.")
print(f"{personaggio3.nome} ha {personaggio3.punti_salute} punti salute.")
print(f"{personaggio4.nome} ha {personaggio4.punti_salute} punti salute.")
print()



personaggio1.usa_abilita_speciale()
personaggio2.usa_abilita_speciale()
personaggio3.usa_abilita_speciale()
personaggio4.usa_abilita_speciale()
print()
print()
print()




personaggio1.attacca(personaggio2)
#personaggio2.subisci_danno(50)         //aggiungi punti danno
print()
print()
personaggio3.attacca(personaggio4)
#personaggio4.subisci_danno(20)         //aggiungi punti danno






