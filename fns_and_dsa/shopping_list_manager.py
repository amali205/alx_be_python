["num1, num2, operation"]
def perform_operation(num1 , num2 , operation):
    if operation == 'add': 
        print(float(num1) + float(num2))
    elif operation == 'subtract':
         print(float(num1) - float(num2))
    elif operation == 'multiply':
         print(float(num1) * float(num2))
    elif operation == 'divide':
      print(float(num1) / float(num2))
    else:
        if num2 == 0 and operation == "divide":
            print("eror")

    
perform_operation(float(input("enter num1 :")), float(input("enter num2 :")),  input("chose the operation ['add', 'subtract', 'multiply', 'divide']"))  
    

