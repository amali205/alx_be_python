def safe_divide(numerator, denominator):
    try:
       num =float(numerator)
       den =float(denominator)
       return num / den

    except ZeroDivisionError :
        return "you can not divide by zero"
    except ValueError :
        return " only integers was accepted"
num = input("enter your first number: ")
den = input("enter your second number: ")
print (safe_divide(num , den))
