task = input (" enter your tasks :")
priority = input("task's priority [high, medium, low] :")

reminder = "is a high priority task that requires immediate attention today!"
Note="is a low priority task. Consider completing it when you have free time."
match priority :
    case "high" : time_bound = input("is the task time-bound [yes or no] : ")
    case "medium" :  time_bound = input("is the task time-bound [yes or no] : ")
    case "low" :  time_bound = input("is the task time-bound [yes or no] : ")
if time_bound == "yes":
         print(task , reminder)
else:
       print (task , Note)
