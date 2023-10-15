def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input temperature in Celsius
celsius = float(input("Enter temperature in degrees Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")