import time, sys

Username='Magnus'
Password='1234'
i=3
usernameInput=''
passwordInput=''

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
time.sleep(0.2)
print('You now have access to your persoanl dashboard')
time.sleep(0.5)
print('Do you want to convert DKK to Euro, or would you like to calculate your postal fee?')
time.sleep(0.5)
print('Enter "C" to convert DKK to Euro')
print('Enter "P" to calculate postal fee')
print('Enter "exit" to log out')

userInput=input()

if userInput=='C':
    kurs=0.13

    print('How many DKK would you like to exchange for Euro?')
    DKKInput=input()
    print('exchange is subject to 2% fee, minimum 0.5 euro')
    euroOutput=int(DKKInput)*kurs
    fee=euroOutput/100*2
    if fee<0.5:
        fee=0.5
    else:
        fee=fee
    finalEuroAmount=euroOutput-fee
    print('You will receive '+str(int(finalEuroAmount))+' euro and you will pay '+str(float(fee))+' euro in fees.')
    print('Thank your for your business.')

elif userInput=='P':
    niveau1=25
    niveau1pris=10
    niveau2=50
    niveau2=18
    niveau3=100
    niveau3pris=25

    print('Hej, jeg er din personlige post-assistent, og kan hjælpe dig med at udregne porto når du vil sende breve.')
    time.sleep(1)
    print('Hvad er vægten på dit brev?')

    while True:
        weight=input()
        try:
            weight = float(weight)
        except:
            print ('Indtast et tal')
            continue
        break 

    if weight<=niveau1:
        print('Your price will be ' + str(niveau1pris) + ' Kr.')
    elif weight<=niveau2:
        print('Your price will be ' + str(niveau2pris) + ' Kr.')
    elif weight<=niveau3:
        print('Your price will be ' + str(niveau3pris) + ' Kr.')
    elif weight>niveau3:
        print('Din pakke er for tung til at blive sendt som brev.')

    time.sleep(1)
    print('Du må have en god dag')


elif userInput=='exit':
    print('You are now logged out')
    sys.exit()

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
