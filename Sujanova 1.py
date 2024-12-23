"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Šujanová
email: lsujanova@seznam.com
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users=[
    {"user": "bob", "password": "123"},
    {"user": "ann", "password": "pass123"},
    {"user": "mike", "password": "password123"},
    {"user": "liz", "password": "pass123"}
]

#Zadání jména a hesla uživatelem
username = input("username: ")
password = input("password: ")
print("-" * 40)

#Ověření, zda je uživatel v listu uživatelů
register = False
for user in users:
    if user["user"] == username and user["password"] == password:
        register = True
        break

#Pokud není uživatel registrovaný, neumožní analýzu textu a ukončí program
if not register:
    print("unregistered user, terminating the program..")
    exit()

#V opačném případě umožní analýzu textu
print("Welcome to the app,", username)
print("We have", len(TEXTS), "texts to be analyzed.")
print("-" * 40)

    # Výběr jednoho z textu (+ověření správnosti zadaného čísla)
choice = int(input("Enter a number btw. 1 and 3 to select: ")) - 1
print("-" * 40)

if choice in [0, 1, 2]:
    # Vybraný text
    selected_text = TEXTS[choice]
else: 
    print("Invalid input, terminating the program..")
    exit()

# Analýza textu
words = selected_text.split()
word_count = len(words)
titlecase_count = sum(1 for word in words if word.istitle())
uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
lowercase_count = sum(1 for word in words if word.islower())
numeric_count = sum(1 for word in words if word.isdigit())
numeric_sum = sum(int(word) for word in words if word.isdigit())

# Výsledky analýzy
print("There are", word_count, "words in the selected text.")
print("There are", titlecase_count, "titlecase words.")
print("There are", uppercase_count, "uppercase words.")
print("There are", lowercase_count, "lowercase words.")
print("There are", numeric_count, "numeric strings.")
print("The sum of all the numbers", numeric_sum)
print("-" * 40)

# Tabulka výskytů podle délky slov
lengths = {}
for word in words:
    cleaned_word = word.strip(",.?!")
    length = len(cleaned_word)
    if length > 0:
        lengths[length] = lengths.get(length, 0) + 1

#Vytvoření jednoduchého grafu
print("LEN| NUMBER OF OCCURENCES")
print("-" * 40)

for length, count in sorted(lengths.items()):
    print(length, " |", "*" * count, count)

    
