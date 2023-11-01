# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:53:06 2023

@author: franc
"""


#forma base della gestione degli errori!
a=5
b=0
try:    
    print(a/b)
except:
    print("Errore!")
print("ma la vita continua!")


#prima variazione:

a=5
b=0    


try:
    print(a/b)
except:
    print ("Errore!")
else:
    print("Tutto è andato bene!") #viene eseguito se non ci sono stati errori e non viene eseguito except!
    


#seconda variazione
    
a=5
b=0
try:
    print(a/b)
except:
    print("Errore!")
else:
    print("tutto ok!")
finally:
    print("viene eseguito comunque")
    
    
    
#esempio con tipi di errori

a=5
b="ciao"
try:
    print(a/b)
except ZeroDivisionError:
    print("Divisione per zero")
except TypeError:
    print("non so calcolare un valore")
except Exception:
    print("errore generico")
else:
    print("tutto ok")
finally:
    print("la vita continua....")



