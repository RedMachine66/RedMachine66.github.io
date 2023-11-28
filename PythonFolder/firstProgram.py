import time

print('Hello!')

time.sleep(0.5)

print('What is your name?')

myName = input()
print('It is good to meet you, ' + myName)
time.sleep(0.9)
print('The length of your name is:')
print(str(len(myName))+' letters.')
time.sleep(1.4)
print('How old are you?')
myAge=input()
time.sleep(0.2)
print('How many fingers do you have?')
fingerCount=input()
time.sleep(0.1)
print('accessing Tesla compute')
time.sleep(0.8)
print('accessing 3-letter agency databases')
time.sleep(1.5)
if int(fingerCount)!=10:
    print('WTF...')
time.sleep(1.8)
print('You will be '+str(int(myAge)+20) + ' years old in two decades')
time.sleep(1.8)
print('___')
if int(fingerCount)==10:
    print('Results show you are human and have nothing to worry about...')
else: 
    print('And having '+str(fingerCount)+' fingers classifies you as an alien, so you will be tracked down and neutralized by the federal government of the USA within 37 hours.')
    time.sleep(2.3)
    print('___')
    print('Do you want a game plan?')
    userConfirm=input()
    if userConfirm=='yes' or 'y':
        print('Call the president, and ask for permission to live')
    else:
        print('Goodbye '+myName)
time.sleep(2.3)
print('______________')
