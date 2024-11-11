# antal lag
n = 5

# fra (hvor står brikkerne)
f = 'A'
# Hjælper (hvilket tårn skal brikkerne rykkes via)
h = 'B'
# mål
t = 'C'

def move(f,t):
    print('Move from ' + f + ' to ' + t)

def moveVia(f, v, t):
    move(f,v)
    move(v,t)

def hanoi(n,f,h,t):
    if n == 0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

hanoi(3,'A', 'B', 'C')

