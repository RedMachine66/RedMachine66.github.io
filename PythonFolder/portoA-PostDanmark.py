import time

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