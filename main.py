
import random

randomNumber=random.randint(1,20)

# print(randomNumber)
userGuess=None

guesses=0

while(userGuess!=randomNumber):
    userGuess=int(input("Enter your guess: "))
    guesses+=1
    if(userGuess==randomNumber):
        print("Bingo...!    \nYou Guessed it Right....!\n")
    else:
        if(userGuess<randomNumber):
            print("\tYou Guessed it wrong...! Enter a Larger number\n")
        else:
            print("\tYou Guessed it wrong...! Enter a Smaller number\n")
    
print("_______________________________________________")
print(f"\tYou guessed the number in {guesses} guesses")

with open("hiscore.txt","r")as f:
    hiscore=int(f.read())

if(guesses<hiscore):
    print("you have just broken the high score..!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))
