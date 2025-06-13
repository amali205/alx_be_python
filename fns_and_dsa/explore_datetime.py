

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date:"))
        future_date = datetime.now() + timedelta(days=days)
        print("The date after", days, "days will be:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the functions
display_current_datetime()
calculate_future_date()
