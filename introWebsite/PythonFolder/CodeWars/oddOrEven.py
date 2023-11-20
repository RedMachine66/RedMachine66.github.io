def odd_or_even(arr):
    arrLen=len(arr)
    n=0
    arrSum=0
    while n < arrLen:
        arrSum=arrSum + arr[n]
        n=n+1
    if arrSum % 2 == 0:
        return 'even'
    elif arrSum % 2 == 1:
        return 'odd'
    
a=odd_or_even([1,2,3,4,3,10,-9])
print(a)