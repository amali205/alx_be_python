Task = input ("Enter your task:")
Priority = input("Priority (high/medium/low):")
Time_bound = input("Is it time-bound?(yes/no): ")
# reminder = "is a high priority task that requires immediate attention today!"
# Note="is a low priority task. Consider completing it when you have free time."
match Priority :
    case "high" : 
        if Time_bound == "yes":
         print(f"Reminder: {Task} is a high priority task that requires immediate attention today!")
    case "medium" : 
         if Time_bound == "yes":
          print(Task)
    case "low" : 
        if Time_bound == "no":
         print(f"Note: {Task} is a low priority task. Consider completing it when you have free time.") 

