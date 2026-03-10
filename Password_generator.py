import random 

possible_digits = ([1, 2, 3, 4, 5, 6, 7, 8, 0])
possible_symbols = (["!", "#", "@", "*"])
possible_vowels = (["a", "e", "i", "o", "u"])

possible_characters = possible_digits + possible_symbols + possible_vowels

p_length = int(input("Desired password lenght?: "))

password = ""

for i in range(p_length):
    chosen_digit = random.choice(possible_characters)
    password += str(chosen_digit)

print(password)

