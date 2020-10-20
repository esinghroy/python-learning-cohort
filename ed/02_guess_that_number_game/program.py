import random

print('''
        --------------------------------------
                GUESS THAT NUMBER GAME        
        --------------------------------------
    ''')

the_number = random.randint(0, 100)
the_guess = -1

while the_guess != the_number:
    guess_text = input("Guess how much money I have in my bank account (hint, it's between 0 and 100 kr): ")
    the_guess  = int(guess_text)

    if the_guess < the_number:
        print(f"Only {the_guess} kr! I'm not that poor! Try again!")
    elif the_guess > the_number:
        print(f"{the_guess} kr! You think I'm that rich?! Try again!")
    else:
        print("You got it! Now give me your bank account details")
