# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:18:36 2023

@author: ASUS
"""
#tutaj zaciągam biblioteki

import os
import random

#Grafika do terminalu (wcale nie zajebałem)
HANGMANPICS = ['''

    +---+    
    |   |
        |
        |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
        |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
    |   |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
   /|   |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
   /|\  |
        |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
   /|\  |
   /    |
        |
        |
===========''', '''

    +---+    
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
===========''']
#szukam sciezki do pliku
def znajdz_sciezke_do_pliku(nazwa_pliku, startowa_sciezka="/"):
    for folder, _, pliki in os.walk(startowa_sciezka):
        if nazwa_pliku in pliki:
            return os.path.join(folder, nazwa_pliku)

    return None
plik= znajdz_sciezke_do_pliku("lista_panstw")
with open(plik, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f]

# Wybieram losowe słowo z listy
slowo = random.choice(lines)

# Tworzę słownik zmiennych dla każdej litery w wybranym słowie
def utworz_zmienne(slowo):
    zmienne = {}
    for litera in slowo:
        zmienne[litera] = False  # Ustawiamy początkową wartość na False
    return zmienne

zmienne = utworz_zmienne(slowo)

# Usuwam znak nowej linii z słowa
zmienne.pop('\n', None)

print(zmienne)

# Definiuję zmienne do gry
life = 7
score = sum(zmienne.values())

# Mechanika gry
while life > 0 and score < len(slowo):
    litera = input("Podaj literę: ")
    if len(litera) !=1:
        print("Zapisz tylko jedną literę!")
    if litera in zmienne and not zmienne[litera]:
        for key in zmienne:
            if key == litera:
                zmienne[key] = True
                score += 1
    else:
        life -= 1

    print("punkty =", score)
    print("życie =", life)
    print(HANGMANPICS[-(7-life)])

if score == len(slowo):
    print("Wygrałeś!")
else:
    print("Przegrałeś. Prawidłowe słowo to:", slowo)
