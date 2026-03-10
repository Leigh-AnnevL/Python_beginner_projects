number = 2000
user_guess = int(input("Guess the random number: "))

while user_guess != number:
    if user_guess > number:
     user_guess = (int(input("Too High! Try again: ")))
    elif user_guess < number:
       user_guess = (int(input("Too Low! Try Again: ")))
       
print("Success")
