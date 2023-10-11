import time, sys

Username='Magnus'
Password='1234'
i=3
usernameInput=''
passwordInput=''
userInput=''

print('Please enter your username')
while usernameInput != Username:
    usernameInput=input()
    if usernameInput != Username:
        print('Account not found, please try again')

print('Account found')
print('Enter password')

while passwordInput!=Password:
    if i==0:
        print('Your account has been locked')
        sys.exit()
    else:
        passwordInput=input()
        if passwordInput!=Password:
            i=i-1
            print('Wrong password')
            print('Attempts remaining: ' + str(i))

print('Access Granted')
print('___________________')
time.sleep(0.2)
print('You now have access to your persoanl dashboard')
time.sleep(0.5)
print('Do you want to convert DKK to Euro, or would you like to calculate your postal fee?')
print('___________________')
time.sleep(0.5)

while userInput != 'x':
    print('Enter "c" to convert DKK to Euro')
    print('Enter "p" to calculate postal fee')
    print('Enter "x" to log out and exit')
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
                    print ('Enter a valid number')
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
            print('Thank your for your business.')
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
                    print ('Indtast et tal')
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
            print('Thank you for your business!')
            print('___________________')
            time.sleep(0.3)
            print('If you want to calculate postal shipping again tap enter')
            print('If you want to return to dashboard enter "n"')
            userInput=input()

print('You have been logged out')





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
