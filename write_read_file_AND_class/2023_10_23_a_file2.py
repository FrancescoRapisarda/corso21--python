#CREO UN FILE CSV E LO LEGGO

clients = [
    {"cliente": "Simone", "saldo": 10},
    {"cliente": "Marco", "saldo": -20},
    {"cliente": "Luca", "saldo": 25},
    {"cliente": "Federico", "saldo": 5},
    {"cliente": "Riccardo", "saldo": 0},
    {"cliente": "Giuseppe", "saldo": -1},
]


fileCsv = open("clienti_saldo.csv", "w")  # Creo un file CSV in modalità scrittura
    
fileCsv.write("cliente, saldo\n\n")

    
for client in clients:
    fileCsv.write(f"{client['cliente']}, {client['saldo']}\n\n")

fileCsv.close()


fileCsv = open("clienti.csv", "r")      # Leggo il file CSV
    
next(fileCsv)   # Ignoro la prima riga (intestazione "cliente || saldo")
    
print("Elenco dei clienti:")
for line in fileCsv:
    client, balance = line.strip().split(",")
    print(f"Cliente: {client}, Saldo: {balance}")