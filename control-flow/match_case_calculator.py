num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation :
     case "+" : 
        Theresult= num1 + num2
        print (f"The result is {Theresult}.")
     case "-" : 
        Theresult= num1 - num2
        print (f"The result is  {Theresult}.")
     case "*" :
        Theresult= num1 * num2
        print (f"The result is {Theresult}.")
     case "/" : 
        if num2 == 0: print ("Cannot divide by zero.")
        else : 
            Theresult= num1 / num2
            print (f"The result is {Theresult}.")
        