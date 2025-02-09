"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lucie Šujanová
email: lsujanova@seznam.cz
"""

import random
import time

def vygeneruj_cislo():
    cislice = list('123456789')  # Cislo nesmi zacinat nulou
    prvni_cislo = random.choice(cislice)
    cislice.remove(prvni_cislo)
    ostatni_cislice = random.sample(cislice + ['0'], 3)  # Dalsi cisla mohou obsahovat nulu
    tajne_cislo = prvni_cislo + ''.join(ostatni_cislice)
    return tajne_cislo

def vyhodnot_tip(tajne_cislo, tip):
    bulls = sum(1 for a, b in zip(tajne_cislo, tip) if a == b)
    cows = sum(1 for c in tip if c in tajne_cislo) - bulls
    return bulls, cows

def hlavni():
    print("Hi there!")
    print("-" * 50)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 50)

    tajne_cislo = vygeneruj_cislo()
    pocet_pokusu = 0
    start_time = time.time()

    while True:
        tip = input("Enter a 4-digit number: ")

        # Kontrola vstupu
        if not tip.isdigit() or len(tip) != 4 or len(set(tip)) != 4 or tip[0] == '0':
            print("Invalid input. Please enter a unique 4-digit number that doesn't start with 0.")
            continue

        pocet_pokusu += 1
        bulls, cows = vyhodnot_tip(tajne_cislo, tip)

        # Výpis výsledku odhadu jednotne/mnozne cislo
        bull_text = "bull" if bulls == 1 else "bulls"
        cow_text = "cow" if cows == 1 else "cows"

        print(f"{bulls} {bull_text}, {cows} {cow_text}")
        
        if bulls == 4:
            end_time = time.time()
            total_time = round(end_time - start_time)
            print(f"Correct, you've guessed the right number {tajne_cislo} in {pocet_pokusu} guesses and {total_time} seconds!")
            print("-" * 50)
            print("That's amazing!")
            break