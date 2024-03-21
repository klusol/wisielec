# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 09:45:34 2024

@author: ASUS
"""
import os
import random


def find_file_path(file_name, startowa_sciezka="/"):
    for folder, _, files in os.walk(startowa_sciezka):
        if file_name in files:
            return os.path.join(folder, file_name)
    return None


def make_variable(word):
    variable = {}
    for letter in word:
        variable[letter] = False
    return variable


hangman_pics = [
    """


    +---+    
    |   |
        |
        |
        |
        |
        |
===========""",
    """


    +---+    
    |   |
    O   |
        |
        |
        |
        |
===========""",
    """


    +---+    
    |   |
    O   |
    |   |
        |
        |
        |
===========""",
    """


    +---+    
    |   |
    O   |
   /|   |
        |
        |
        |
===========""",
    """


    +---+    
    |   |
    O   |
   /|\  |
        |
        |
        |
===========""",
    """


    +---+    
    |   |
    O   |
   /|\  |
   /    |
        |
        |
===========""",
    """


    +---+    
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
===========""",
]

file_path = find_file_path("lista_panstw.txt", os.path.dirname(__file__))
with open(file_path, "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]

word = random.choice(lines).upper()
word_print = ["_" for _ in word]
missed_letters = []

variable = make_variable(word)
variable.pop("\n", None)


def main():
    life = 7
    score = sum(variable.values())
    print(word_print)
    while life > 0 and score < len(word):
        letter = input("Podaj literę: ").upper()
        if len(letter) != 1:
            print("Podaj tylko jedną literę!")
            print("Punkty =", score)
            print("Życie =", life)
            print(hangman_pics[7 - life])
            print("Słowo:", " ".join(word_print))
            print("Pomyłkowe litery:", missed_letters)
        elif letter in variable and not variable[letter]:
            for i, key in enumerate(word):
                if key == letter:
                    variable[key] = True
                    word_print[i] = letter
                    score += 1
                print("Punkty =", score)
                print("Życie =", life)
                print(hangman_pics[7 - life])
                print("Słowo:", " ".join(word_print))
                print("Pomyłkowe litery:", missed_letters)
        else:
            life -= 1
            missed_letters.append(letter)
            print("Punkty =", score)
            print("Życie =", life)
            print(hangman_pics[7 - life])
            print("Słowo:", " ".join(word_print))
            print("Pomyłkowe litery:", missed_letters)
            if score == len(word):
                print("Wygrałeś!")
            elif life == 0:
                print("Przegrałeś. Prawidłowe słowo to:", word)


if __name__ == "__main__":
    main()
