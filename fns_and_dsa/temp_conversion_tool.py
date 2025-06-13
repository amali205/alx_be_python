# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the global factor
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the global factor
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert:")
        temperature = float(temp_input)  # Validate numeric input

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

        if unit == 'C':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result:.2f}°F")
        elif unit == 'F':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print("Error:", ve)
        print("Invalid temperature. Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()
