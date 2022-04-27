import random

play = "y"

while play.lower() == "y":
    import subprocess as sp
    sp.call('cls', shell=True)
    num = random.randint(1, 999)
    count = 1

    guess = int(input("Guess a Number Between 1 - 1000: "))

    while guess != num:
        if guess <= 1 or guess >=1000:
            guess = int(input("OK that wasnt between 1-1000.  Guess again: "))
        elif num > guess:
            guess = int(input("Sorry, the number is higher.  Guess again: "))
            count +=1
        else:
            guess = int(input("Sorry, the number is lower.  Guess again: "))
            count +=1

    print(f"\n\nGreat Job!  You guessed the right number which was {num} in {count} tries.")

    play = input("\n\n Enter Y to play again or ENTER to exit: ")
