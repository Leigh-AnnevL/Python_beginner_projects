number = 1234
user_guess = int(input("Guess the random number: "))

while user_guess != number:
    user_guess = (int(input("Wrong Answer, try again!: ")))

print("Success")