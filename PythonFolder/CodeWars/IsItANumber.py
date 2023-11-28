def is_digit(s):
    try:
        float(s)
    except:
        return False
    return True

a=is_digit('5.000')
print(a)