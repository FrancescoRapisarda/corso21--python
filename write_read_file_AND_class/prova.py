def friend(x):
    return [ i for i in x if len(i) == 4 ]  # simile a filter


list = ["Francesco", "Febe", "Simone", "1234", "34000"]
result = friend(list)
print(result)   # Restituirà ["ciao", "test"]


