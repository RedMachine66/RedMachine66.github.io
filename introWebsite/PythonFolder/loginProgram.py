import time, sys

Username='Magnus'
Password='1234'
i=3


print('Please enter your username')
while True:
    usernameInput=input()
    if usernameInput != Username:
        print('Account not found')
        continue
    else:
        print('Enter password')
        while True:
            if i==0:
                print('Your account has been locked')
                sys.exit()
            else:
                passwordInput=input()
                if passwordInput!=Password:
                    i=i-1
                    print('Wrong password')
                    print('Attempts remaining: ' + str(i))
                    continue
                else:
                    break
    break
print('Access Granted')




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
