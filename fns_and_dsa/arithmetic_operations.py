["num1, num2, operation"]
def perform_operation(num1 , *num2 , **operation):
    if operation == 'add': 
        print(float(num1) + float(num2))
    elif operation == 'subtract':
         print(float(num1) - float(num2))
    elif operation == 'multiply':
         print(float(num1) * float(num2))
    if operation == 'divide':
      print(float(num1) / float(num2))

print("Arithmetic Operations")    
perform_operation(float(input("Enter the first number:")), float(input("Enter the second number:")),  str(input("Enter the operation (add, subtract, multiply, divide):")))  
    

