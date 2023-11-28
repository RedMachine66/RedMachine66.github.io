startRange=2
stopRange=21
stepRange=2

while startRange != 11:
    for i in range(startRange, stopRange, stepRange):
        print(i)
    startRange=startRange+1
    stopRange=stopRange+10
    stepRange=stepRange+1
    print()
