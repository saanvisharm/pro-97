import random
print("Number Guessing Game")
number=random.randint(1,9)
chance=0
print("Guess a number between 1-9.")
while chance < 5:
    guess=int(input("enter your guess"))
    if guess==number:
        print("Congratulations!! You Won!!")   
        break

    elif guess<number:
        print("Close but the guess's number is low")
    else:
        print("Guess is too high")
    chance=chance+1
if not chance <5:
    print("You lose! Try Again!",number)