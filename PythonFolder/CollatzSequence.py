def collatz(number):
    if number % 2 == 0:
        numOut=number//2
        return numOut
    elif number % 2 == 1:
        numOut=3*number+1
        return numOut

print('Collatz Sequence')
print('Write a number')

number=None
numOut=int(input())

while numOut != 1:
    numOut=collatz(numOut)
    print(numOut)