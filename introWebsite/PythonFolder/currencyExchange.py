kurs=0.13

print('How many DKK would you like to exchange for Euro?')
DKKAmount=input()
print('exchange is subject to 2% fee, minimum 0.5 euro')
euroAmount=int(DKKAmount)*kurs
fee=euroAmount/100*2
if fee<0.5:
    fee=0.5
else:
    fee=fee
finalEuroAmount=euroAmount-fee
print('You will receive '+str(int(finalEuroAmount))+' euro and you will pay '+str(float(fee))+' euro in fees.')
print('Thank your for your business.')