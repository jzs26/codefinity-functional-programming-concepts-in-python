# Step 1: Define the list of temperatures in Celsius
temp_celsius = [0, 25, 30, 40, 100]

# Step 2: Create a custom function for conversion
def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Step 3: Use map() with the custom function
fahrenheit = map(celsius_to_fahrenheit, temp_celsius)

# Step 4: Convert the map object to a list and print
temp_fahrenheit_list = list(fahrenheit)
print(temp_fahrenheit_list)