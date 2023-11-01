import moduli as am             #crea modulo   e un   #alias am    (va a prendere TUTTO il modulo)

import platform                 #modulo built in (platform)

import math                     #modulo built in (math)

from moduli import persona1     #importare SOLO UNA PARTE del modulo

print(persona1["nome"])


am.saluta("Luca")

x = am.persona1["nome"]
am.saluta(x)


y = platform.system()
print(y)


print(math.floor(2.90))
print(math.sqrt(4))
print(dir(math))                 #funzione dir()