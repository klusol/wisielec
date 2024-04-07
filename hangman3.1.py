# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:44:50 2024

@author: ASUS
"""
import os
import random

def find_file_path(file_name, starting_path="/"):
    for folder, _, files in os.walk(starting_path):
        if file_name in files:
            return os.path.join(folder, file_name)
    return None

def slice_word(word):
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

def main():
    while True:  # Pętla, która pozwala na powtórzenie gry bez użycia rekursji
        life = 7
        word = random.choice(lines).upper()
        word_print = ["_" for _ in word]
        missed_letters = []
        variable = slice_word(word)
        variable.pop("\n", None)
        score = sum(variable.values())

        while life > 0 and score < len(word):
            print(word_print)
            letter = input("Podaj literę: ").upper()
            if len(letter) != 1:
                print("Podaj tylko jedną literę!")
                continue

            if letter in variable and not variable[letter]:
                for i, key in enumerate(word):
                    if key == letter:
                        variable[key] = True
                        word_print[i] = letter
                        score += 1
                print(f"Punkty = {score}\n"
                      f"Życie = {life}\n"
                      f"{hangman_pics[7 - life]}\n"
                      f"(Słowo: {' '.join(word_print)})\n"
                      f"Pomyłkowe litery: {', '.join(missed_letters)}")
            else:
                life -= 1
                missed_letters.append(letter)
                print(f"Punkty = {score}\n"
                      f"Życie = {life}\n"
                      f"{hangman_pics[7 - life]}\n"
                      f"(Słowo: {' '.join(word_print)})\n"
                      f"Pomyłkowe litery: {', '.join(missed_letters)}")

            if score == len(word):
                print("Wygrałeś!")
                break  # Przerwij pętlę, gdy gracz wygra
            elif not life:
                print(f"Przegrałeś. Prawidłowe słowo to: {word}")
                break  # Przerwij pętlę, gdy gracz przegra

        if input("Jeżeli chcesz grać dalej nacinij 'x': ").lower() != "x":
            break  # Jeśli gracz nie chce grać dalej, przerwij główną pętlę

if __name__ == "__main__":
    main()
