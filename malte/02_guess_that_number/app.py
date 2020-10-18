import random
from timeit import default_timer as timer


print("-" * 38)
print(" " * 9 + "GUESS THE NUMBER APP")
print("-" * 38)

the_number = random.randint(0, 100)
the_guess = -1
start_time = timer()

while the_guess != the_number:

    the_guess = input("Guess a number between 0 and 100: ")

    try:
        the_guess = int(the_guess)
        if the_guess < 0 or the_guess > 100:
            raise ValueError
    except ValueError:
        print(f"'{the_guess}' is not a vaild number! Try again!")
        continue

    if the_guess == 42:
        print("Yes! 42 is always the correct anwser!")
        break

    if the_guess == the_number:
        start_end = timer()
        print(
            f"Awesome! You got it in {start_end - start_time:.1f} seconds!! Now go back to work!"
        )

    if the_guess > the_number:
        print(f"Too high man!")

    if the_guess < the_number:
        print("Too low man!")
