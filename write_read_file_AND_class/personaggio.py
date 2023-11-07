class Personaggio:
    
    def __init__(self, nome, livello, punti_salute):
        self.nome = nome
        self.livello = livello
        self.punti_salute = punti_salute


    def attacca(self, bersaglio):
        danno = self.livello * 10    # Calcola il danno dell'attacco in base al livello del personaggio
        print(f"{self.nome} attacca {bersaglio.nome} e infligge {danno} punti di danno.")
        bersaglio.subisci_danno(danno)
        


    def subisci_danno(self, danno):
        self.punti_salute -= danno  # Sottrai i punti ferita subiti dal personaggio
        if self.punti_salute <= 0:
            print(f"{self.nome} e'stato sconfitto!")
        else:
            print(f"A {self.nome} gli rimangono {self.punti_salute} punti!")




class PersonaggioSpecifico(Personaggio):
    def __init__(self, nome, livello, punti_salute, arma, abilita_speciale):
        # Chiamiamo il costruttore della superclasse
        super().__init__(nome, livello, punti_salute)
        # Aggiungiamo attributi specifici alla sottoclasse
        self.arma = arma
        self.abilita_speciale = abilita_speciale

    def usa_abilita_speciale(self):
        # Implementiamo un metodo specifico per l'abilità speciale
        print(f"{self.nome} utilizza l'abilita' speciale: {self.abilita_speciale}")



# Esempio di utilizzo della sottoclasse con un personaggio specifico
personaggio1 = PersonaggioSpecifico("Aragorn", 15, 150, "Spada di Anduril", "Risolutezza")
personaggio2 = PersonaggioSpecifico("Legolas", 8, 200, "Bastone allungabile", "Velocita")
personaggio3 = PersonaggioSpecifico("Federik", 2, 290, "Manganello", "Logica")


print(f"{personaggio1.nome} di livello {personaggio1.livello}.")
print(f"Usa {personaggio1.arma} come arma principale.")
print()

print(f"{personaggio2.nome} di livello {personaggio2.livello}.")
print(f"Usa {personaggio2.arma} come arma principale.")
print()

print(f"{personaggio3.nome} di livello {personaggio3.livello}.")
print(f"Usa {personaggio3.arma} come arma principale.")
print()

print(f"{personaggio1.nome} ha {personaggio1.punti_salute} punti salute.")
print(f"{personaggio2.nome} ha {personaggio2.punti_salute} punti salute.")
print(f"{personaggio3.nome} ha {personaggio3.punti_salute} punti salute.")
print()

# Esempio di utilizzo dell'abilità speciale
personaggio1.usa_abilita_speciale()
personaggio2.usa_abilita_speciale()
personaggio3.usa_abilita_speciale()
print()
print()
print()


# Esempio di attacco
personaggio1.attacca(personaggio2)
personaggio2.attacca(personaggio3)
print()

# Esempio di subire danni
personaggio2.subisci_danno(50)
personaggio3.subisci_danno(20)


