#sabato 28.10.2023
#Classi e Oggetti

""" 
Una classe è un modello o un prototipo che definisce la struttura di un oggetto.
Le classi rappresentano un tipo di dati astratto che include attributi (variabili) e metodi (funzioni) che operano su questi attributi.
Le classi sono come i "mattoni" con cui si costruiscono gli oggetti. 
Definiscono quali dati possono essere memorizzati in un oggetto e quali operazioni possono essere eseguite su di esso.
"""


#Crea una classe
class Person:
    def __init__(self, name, surname):         #costruttore
        self.name = name
        self.surname = surname
    
    def saluta(self):
        print("Ciao, mi chiamo " + self.name)

        
"""
Un oggetto è un'istanza di una classe. 
È una variabile che rappresenta una copia della struttura definita dalla classe.
Gli oggetti hanno attributi (variabili) e possono eseguire metodi (funzioni) specifici definiti nella classe.
Ogni oggetto ha uno stato e un comportamento definiti dalla classe di cui è un'istanza.
"""

#Istanziare l'oggetto
persona1 = Person("Francesco", "Rapisarda")
print(persona1.name)
persona1.saluta()

persona2 = Person("Davide", "Rapisarda")
print(persona2.name)
persona2.saluta()



#Ereditarietà
class Teacher(Person):
    pass

teacher1 = Teacher("Giuliana", "Cacciola")
print(teacher1.name)
print(teacher1.surname)


#---------------------------------------

class Teacher(Person):
    def __init__(self, name, surname):          #costruttore
        super().__init__(name, surname)         #super prende attributi della classe ereditata!
        
    def saluta(self):
        print("Buongiorno ragazzi, il mio nome e' " + self.name + " " + self.surname + "!")
        
    def voto(self):
        print("Vi daro' un voto nella prova finale!")

teacher2 = Teacher("Carlo", "Leonardi")
print(teacher2.name)
print(teacher2.surname)
teacher2.saluta()
teacher2.voto()



