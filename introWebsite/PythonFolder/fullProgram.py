import time, sys, cowsay, pyfiglet, json, random
from termcolor import colored

userInput=''

# Database, Account List:
AL = {
    'Magnus':'1234',
    'Test':'4321',
    'Rasmus':'unicorn',
    'incognito':'password'
}

banner = pyfiglet.Figlet(font='slant')
print(banner.renderText('Dash Corp'))

print(colored('Please enter your username', 'green'))
while True:
    usernameInput=''
    usernameInput=input()
    if usernameInput not in AL:
        print('Account not found, please try again')
        continue
    break

print('Account found')
print(colored('Enter password', 'green'))

i=3
while True:
    passwordInput=''
    if i==0:
        print(colored('Your account has been locked', 'red'))
        sys.exit()
    else:
        passwordInput=input()
        if passwordInput != AL[usernameInput]:
            i=i-1
            print(colored('Access Denied', 'red'))
            print('Attempts remaining: ' + str(i))
        else:
            break

print(colored('Access Granted', 'green'))
print('___________________')
time.sleep(0.2)
banner = pyfiglet.Figlet(font='slant')
print(banner.renderText('Welcome'))
time.sleep(0.2)
print(colored(usernameInput,'blue') + ', you now have access to your personal dashboard')
time.sleep(0.5)
print('Do you want to convert DKK to Euro, or would you like to calculate your postal fee?')
time.sleep(0.5)

while userInput != 'x':
    print('___________________')
    print('')
    print('Enter ' + colored('"c"', 'green') + ' to convert DKK to Euro')
    print('Enter ' + colored('"p"', 'green') + ' to calculate postal fee')
    print('Enter ' + colored('"g"', 'green') + ' to play a game')
    print('Enter ' + colored('"x"', 'green') + ' to log out and exit')
    print('___________________')

    userInput=input()

    if userInput=='c':
        while userInput != 'n':
            kurs=0.13
            print('How many DKK would you like to exchange for Euro?')
            while True:
                DKKInput=input()
                try:
                    DKKInput = float(DKKInput)
                except:
                    print (colored('Enter a valid number', 'yellow'))
                    continue
                break 
            print('exchange is subject to 2% fee, minimum 0.5 euro')
            euroOutput=int(DKKInput)*kurs
            fee=euroOutput/100*2
            if fee<0.5:
                fee=0.5
            else:
                fee=fee
            finalEuroAmount=euroOutput-fee
            time.sleep(0.2)
            print('___________________')
            print('You will receive '+str(int(finalEuroAmount))+' euro and you will pay '+str(float(fee))+' euro in fees.')
            time.sleep(0.2)
            print(colored('Thank your for your business.', 'blue'))
            print('___________________')
            time.sleep(0.5)
            print('If you want to convert again tap enter')
            print('If you want to return to dashboard enter "n"')
            userInput=input()


    elif userInput=='p':
        while userInput != 'n':
            niveau1=25
            niveau1pris=10
            niveau2=50
            niveau2=18
            niveau3=100
            niveau3pris=25

            print('Hello, I am your personal shipping cost assistant.')
            time.sleep(0.3)
            print('What is the weight of your letter?')

            while True:
                weight=input()
                try:
                    weight = float(weight)
                except:
                    print (colored('Enter a valid number', 'yellow'))
                    continue
                break 
            time.sleep(0.2)
            if weight<=niveau1:
                print('Your price will be ' + str(niveau1pris) + ' Kr.')
            elif weight<=niveau2:
                print('Your price will be ' + str(niveau2pris) + ' Kr.')
            elif weight<=niveau3:
                print('Your price will be ' + str(niveau3pris) + ' Kr.')
            elif weight>niveau3:
                print('Your package is too heavy to send as a letter.')

            print('___________________')
            time.sleep(0.5)
            print(colored('Thank your for your business.', 'blue'))
            print('___________________')
            time.sleep(0.3)
            print('If you want to calculate postal shipping again tap enter')
            print('If you want to return to dashboard enter "n"')
            userInput=input()

    elif userInput=='g':
        while userInput != 'n':
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
            print('___________________')
            time.sleep(0.3)
            print('If you want to play again tap enter')
            print('If you want to return to dashboard enter "n"')
            userInput=input()

print('___________________')
print(colored('You have been logged out', 'yellow'))





# old code
# print('Please enter your username')
# while True:
#     usernameInput=input()
#     if usernameInput != Username:
#         print('Account not found')
#         continue
#     else:
#         print('Enter password')
#         while True:
#             if i==0:
#                 print('Your account has been locked')
#                 sys.exit()
#             else:
#                 passwordInput=input()
#                 if passwordInput!=Password:
#                     i=i-1
#                     print('Wrong password')
#                     print('Attempts remaining: ' + str(i))
#                     continue
#                 else:
#                     break
#     break
# print('Access Granted')




# old code
# usernameinput=input()
# if usernameinput==Username:
#     print('Please enter password')
#     passwordinput=input()
#     if passwordinput==Password:
#         print('Access Granted')
#     else:
#         print('Access Denied')
# else:
#     print('Username not found')
