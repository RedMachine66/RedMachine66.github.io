import time, sys, json

i=3
usernameInput=''
passwordInput=''

accountDatabase = 'accountDatabase.json'

try:
    with open(accountDatabase, 'r') as accountFile:
        accountData = json.load(accountFile)
except (FileNotFoundError, json.JSONDecodeError):
    accountData = {}

print('Please enter your username')
while True:
    usernameInput=input()
    if usernameInput not in accountData:
        print('Account not found, please try again')
        continue
    break

print('Account found')
print('Enter password')

while True:
    if i==0:
        print('Your account has been locked')
        sys.exit()
    else:
        passwordInput=input()
        if passwordInput != accountData[usernameInput]:
            i=i-1
            print('Wrong password')
            print('Attempts remaining: ' + str(i))
        else:
            break

print('Access Granted')



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
