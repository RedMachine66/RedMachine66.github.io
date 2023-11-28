import random

def numberGuess(num):
    if userInput > magicNumber:
        return "No, it's lower"
    elif userInput < magicNumber:
        return "No, it's higher"
    elif userInput == magicNumber:
        return 'Damn it, you got it'

magicNumber=random.randint(1,20)

print("Guess which number between 1 and 20 I'm thinking about")

i=0
userInput=None

while userInput != magicNumber and i != 3:
    userInput=int(input())
    print(numberGuess(userInput))
    i += 1

print(f"you used {i} geusses")

if userInput == magicNumber:
    print('Good work')
elif i == 3:
    print("Better luck next time. You've used all your guesses")
