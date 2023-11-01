# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

name = input('dammi una stringa a piacere')
count = 0
#vocali = ['a', 'e', 'i', 'o', 'u']

for carattere in name:
    if carattere.lower() in "aeiou":
        count += 1

print(f"La stringa '{name}' contiene {count} vocali.")



