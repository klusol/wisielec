from pathlib import PureWindowsPath
import random

# slice word to single letter stored in dict in order to in order to guess them.When letters are guessed value switch to true 
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
    """
    +---+    
    |   |
    O   |
   /|\  |
   / \  |
        |
        |
==========="""
]

p = PureWindowsPath(__file__)
with open(p.with_name("lista_panstw.txt"), "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]

def main():
    while True:  
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
