Username='Magnus'
Password='1234'

print('Please enter your username')
usernameinput=input()
if usernameinput==Username:
    print('Please enter password')
    passwordinput=input()
    if passwordinput==Password:
        print('Access Granted')
    else:
        print('Access Denied')
else:
    print('Username not found')
