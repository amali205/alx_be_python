Task = input (" enter your tasks :")
Priority = input("task's priority [high, medium, low] :")
Time_bound = input("is the task time-bound [yes or no] : ")
reminder = "is a high priority task that requires immediate attention today!"
Note="is a low priority task. Consider completing it when you have free time."
match Priority :
    case "high" : 
        if Time_bound == "yes":
         print(Task , reminder)
    case "medium" : 
         if Time_bound == "yes":
          print(Task , reminder)
    case "low" : 
        if Time_bound == "no":
         print(Task , Note) 

