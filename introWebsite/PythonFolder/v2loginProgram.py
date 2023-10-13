import time, sys

i=3
usernameInput=''
passwordInput=''

AL = {
    'Magnus':'1234',
    'Test':'4321'
}

print('Please enter your username')
while True:
    usernameInput=input()
    if usernameInput not in AL:
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
        if passwordInput != AL[usernameInput]:
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
