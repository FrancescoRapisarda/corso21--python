name="francesco"
#name = input('dammi una stringa a piacere')
count = 0
#vocali = ['a', 'e', 'i', 'o', 'u']

for carattere in name:
    if carattere.lower() in "aeiou":
        count += 1

print(f"La stringa '{name}' contiene {count} vocali.")



def conta_vocali(name):
    count = 0
    for carattere in name:
        if carattere.lower() in "aeiou":
            count += 1
    return count


def saluto(nome):
    #esempio di funzione non produttiva, cioè senza return
    print("ciao", nome, "!")
    
saluto("pippo")

type(saluto) #function



