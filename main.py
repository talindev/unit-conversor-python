# PYTHON Unit Converter - Training personal Project
# GITHUB: talindev

print("WELCOME TO MY UNIT CONVERSION PROGRAM! :)")
print("Choose a category:")
option = int(input("1. Pressure\n2. Velocity\n3. Temperature\n4. Length\n5. Leave!\n\nOption: "))

# Unit conversion functions

# Pressure
def pressureCalc():
    entry = input("Type your entry (number (space) unit): ").lower()
    entry = entry.split(" ")
    reverseEntry = entry[::-1]

    pressureOption = int(input("Choose to which unit you want to convert!\n1. mmHg\n2. Pa\n3. N/M2\n\n"))
    if pressureOption < 0 or pressureOption > 3:
        print("INCORRECT VALUE!")
    else:
        pass

    # Pressure conversion if-elif chain
    # Pascal input
    if reverseEntry[0] == "pa" and pressureOption == 1:
        pressureResult = (float(entry[0])) * 0.0075
        print(f"RESULT: {pressureResult:,} mmHg")
    elif reverseEntry[0] == "pa" and pressureOption == 2:
        print("error.. do not choose equal units")
    elif reverseEntry[0] == "pa" and pressureOption == 3:
        pressureResult = float(entry[0])
        print(f"RESULT: {pressureResult:,} N/M2")
    # mm of mercury input
    elif reverseEntry[0] == "mmhg" and pressureOption == 1:
        print("error.. do not choose equal units")
    elif reverseEntry[0] == "mmhg" and pressureOption == 2:
        pressureResult = (float(entry[0]) * 133.32)
        print(f"RESULT: {pressureResult:,} Pa")
    elif reverseEntry[0] == "mmhg" and pressureOption == 3:
        pressureResult = (float(entry[0]) * 133.32)
        print(f"RESULT: {pressureResult:,} N/M2")
    # Newton per meter squared input
    elif reverseEntry[0] == "n/m2" and pressureOption == 1:
        pressureResult = (float(entry[0])) * 0.0075
        print(f"RESULT: {pressureResult:,} mmHg")
    elif reverseEntry[0] == "n/m2" and pressureOption == 2:
        pressureResult = float(entry[0])
        print(f"RESULT: {pressureResult:,} Pa")
    elif reverseEntry[0] == "n/m2" and pressureOption == 3:
        print("error.. do not choose equal units")
    # Default error
    else:
        print("error......not identified // incorrect value or unit!")

# Velocity
def velocityCalc():
    entry = input("Type your entry (number (space) unit): ").lower()
    entry = entry.split(" ")
    reverseEntry = entry[::-1]

    velocityOption = int(input("Choose to which unit you want to convert!\n1. km/h\n2. m/s\n\n"))
    if velocityOption < 0 or velocityOption > 2:
        print("INCORRECT VALUE!")
    else:
        pass

    # Velocity conversion if-elif chain
    # Kilometers per hour input
    if (reverseEntry[0] == "km/h" or reverseEntry[0] == "kmh") and velocityOption == 1:
        print("error.. do not choose equal units")
    elif (reverseEntry [0] == "km/h" or reverseEntry[0] == "kmh") and velocityOption == 2:
        velocityResult = (float(entry[0])) / 3.6
        print(f"RESULT: {velocityResult:,} m/s")
    # Meter per second input
    elif (reverseEntry[0] == "m/s" or reverseEntry[0] == "ms") and velocityOption == 1:
        velocityResult = (float(entry[0])) * 3.6
        print(f"RESULT: {velocityResult:,} km/h")
    elif (reverseEntry[0] == "m/s" or reverseEntry[0] == "ms") and velocityOption == 2:
        print("error.. do not choose equal units")
    # Default error
    else:
        print("error......not identified // incorrect value or unit!")

# Temperature
def tempCalc():
    entry = input("Type your entry (number (space) unit): ").lower()
    entry = entry.split(" ")
    reverseEntry = entry[::-1]

    tempOption = int(input("Choose to which unit you want to convert!\n1. Celsius\n2. Fahrenheit\n3. Kelvin\n\n"))
    if tempOption < 0 or tempOption > 3:
        print("INCORRECT VALUE!")
    else:
        pass
    
    # Temperature conversion if-elif chain
    # Celsius input
    if (reverseEntry[0] == "c" or reverseEntry[0] == "celsius" or reverseEntry[0] == "°c") and tempOption == 1:
        print("error.. do not choose equal units")
    elif (reverseEntry[0] == "c" or reverseEntry[0] == "celsius" or reverseEntry[0] == "°c") and tempOption == 2:
        tempResult = ((float(entry[0])) * 1.8) + 32
        print(f"RESULT: {tempResult:,} °F")
    elif (reverseEntry[0] == "c" or reverseEntry[0] == "celsius" or reverseEntry[0] == "°c") and tempOption == 3:
        tempResult = (float(entry[0])) + 273.15
        print(f"RESULT: {tempResult:,} K")
    # Fahrenheit input
    elif (reverseEntry[0] == "f" or reverseEntry[0] == "fahrenheit" or reverseEntry[0] == "°f") and tempOption == 1:
        tempResult = (((float(entry[0])) - 32) * 5) / 9
        print(f"RESULT: {tempResult:,} °C")
    elif (reverseEntry[0] == "f" or reverseEntry[0] == "fahrenheit" or reverseEntry[0] == "°f") and tempOption == 2:
        print("error.. do not choose equal units")
    elif (reverseEntry[0] == "f" or reverseEntry[0] == "fahrenheit" or reverseEntry[0] == "°f") and tempOption == 3:
        celsius = (((float(entry[0])) - 32) * 5) / 9
        tempResult = celsius + 273.15
        print(f"RESULT: {tempResult:,} K")
    # Kelvin input
    elif (reverseEntry[0] == "k" or reverseEntry[0] == "kelvin") and tempOption == 1:
        tempResult = (float(entry[0])) - 273.15
        print(f"RESULT: {tempResult:,} °C")
    elif (reverseEntry[0] == "k" or reverseEntry[0] == "kelvin") and tempOption == 2:
        celsius = (float(entry[0])) - 273.15
        tempResult = (celsius * 1.8) + 32
        print(f"RESULT: {tempResult:,} °F")
    elif (reverseEntry[0] == "k" or reverseEntry[0] == "kelvin") and tempOption == 3:
        print("error.. do not choose equal units")
    # Default error
    else:
        print("error......not identified // incorrect value or unit!")

# Length
def lengthCalc():
    entry = input("Type your entry (number (space) unit): ").lower()
    entry = entry.split(" ")
    reverseEntry = entry[::-1]

    lenOption = int(input("Choose to which unit you want to convert!\n1. Meters\n2. Kilometers\n3. Miles\n4. Centimeters\n5. Milimeters\n6. Light-Years\n\n"))
    if lenOption < 0 or lenOption > 6:
        print("INCORRECT VALUE!")
    else:
        pass

    # Length conversion if-elif chain
    # Meter input
    if reverseEntry[0] == "m" and lenOption == 1:
        print("error.. do not choose equal units")
    elif reverseEntry[0] == "m" and lenOption == 2:
        lenResult = (float(entry[0])) / 1000
        print(f"RESULT: {lenResult:,} km")
    elif reverseEntry[0] == "m" and lenOption == 3:
        lenResult = (float(entry[0])) * 0.000621371
        print(f"RESULT: {lenResult:,} mi")
    elif reverseEntry[0] == "m" and lenOption == 4:
        lenResult = (float(entry[0])) * 100
        print(f"RESULT: {lenResult:,} cm")
    elif reverseEntry[0] == "m" and lenOption == 5:
        lenResult = (float(entry[0])) * 1000
        print(f"RESULT: {lenResult:,} mm")
    elif reverseEntry[0] == "m" and lenOption == 6:
        lenResult = (float(entry[0])) / 9460730472580000
        print(f"RESULT: {lenResult:,} ly")
    # Kilometer input
    elif reverseEntry[0] == "km" and lenOption == 1:
        lenResult = (float(entry[0])) * 1000
        print(f"RESULT: {lenResult:,} m")
    elif reverseEntry[0] == "km" and lenOption == 2:
        print("error.. do not choose equal units")
    elif reverseEntry[0] == "km" and lenOption == 3:
        lenResult = (float(entry[0])) * 0.621371
        print(f"RESULT: {lenResult:,} mi")
    elif reverseEntry[0] == "km" and lenOption == 4:
        lenResult = (float(entry[0])) * 100000
        print(f"RESULT: {lenResult:,} cm")
    elif reverseEntry[0] == "km" and lenOption == 5:
        lenResult = (float(entry[0])) * 1000000
        print(f"RESULT: {lenResult:,} mm")
    elif reverseEntry[0] == "km" and lenOption == 6:
        lenResult = (float(entry[0])) / 9460730472580
        print(f"RESULT: {lenResult:,} ly")
    # Miles input
    elif reverseEntry[0] == "mi" and lenOption == 1:
        lenResult = (float(entry[0])) * 1609.344
        print(f"RESULT: {lenResult:,} m")
    elif reverseEntry[0] == "mi" and lenOption == 2:
        lenResult = (float(entry[0])) * 1.609344
        print(f"RESULT: {lenResult:,} km")
    elif reverseEntry[0] == "mi" and lenOption == 3:
        print("error.. do not choose equal units")
    elif reverseEntry[0] == "mi" and lenOption == 4:
        lenResult = (float(entry[0])) * 160934.4
        print(f"RESULT: {lenResult:,} cm")
    elif reverseEntry[0] == "mi" and lenOption == 5:
        lenResult = (float(entry[0])) * 1609344
        print(f"RESULT: {lenResult:,} mm")
    elif reverseEntry[0] == "mi" and lenOption == 6:
        lenResult = (float(entry[0]) * 1.609344) / 9460730472580
        print(f"RESULT: {lenResult:,} ly")
    # Centimeters input
    elif reverseEntry[0] == "cm" and lenOption == 1:
        lenResult = (float(entry[0])) * 0.01
        print(f"RESULT: {lenResult:,} m")
    elif reverseEntry[0] == "cm" and lenOption == 2:
        lenResult = (float(entry[0])) * 0.00001
        print(f"RESULT: {lenResult:,} km")
    elif reverseEntry[0] == "cm" and lenOption == 3:
        lenResult = (float(entry[0])) * 0.0000062137
        print(f"RESULT: {lenResult:,} mi")
    elif reverseEntry[0] == "cm" and lenOption == 4:
        print("error.. do not choose equal units")
    elif reverseEntry[0] == "cm" and lenOption == 5:
        lenResult = (float(entry[0])) * 10
        print(f"RESULT: {lenResult:,} mm")
    elif reverseEntry[0] == "cm" and lenOption == 6:
        lenResult = (float(entry[0])) / 946073047258000000000
        print(f"RESULT: {lenResult:,} ly")
    # Milimeters input
    elif reverseEntry[0] == "mm" and lenOption == 1:
        lenResult = (float(entry[0])) * 0.001
        print(f"RESULT: {lenResult:,} m")
    elif reverseEntry[0] == "mm" and lenOption == 2:
        lenResult = (float(entry[0])) * 0.000001
        print(f"RESULT: {lenResult:,} km")
    elif reverseEntry[0] == "mm" and lenOption == 3:
        lenResult = (float(entry[0])) * 0.00000062137
        print(f"RESULT: {lenResult:,} mi")
    elif reverseEntry[0] == "mm" and lenOption == 4:
        lenResult = (float(entry[0])) * 0.1
        print(f"RESULT: {lenResult:,} cm")
    elif reverseEntry[0] == "mm" and lenOption == 5:
        print("error.. do not choose equal units")
    elif reverseEntry[0] == "mm" and lenOption == 6:
        lenResult = (float(entry[0])) / 9460730472580000000000
        print(f"RESULT: {lenResult:,} ly")
    # Light-years input
    elif reverseEntry[0] == "ly" and lenOption == 1:
        lenResult = (float(entry[0])) * 9460730472580000
        print(f"RESULT: {lenResult:,} m")
    elif reverseEntry[0] == "ly" and lenOption == 2:
        lenResult = (float(entry[0])) * 9460730472580
        print(f"RESULT: {lenResult:,} km")
    elif reverseEntry[0] == "ly" and lenOption == 3:
        lenResult = (float(entry[0])) * 5878000000000000000
        print(f"RESULT: {lenResult:,} mi")
    elif reverseEntry[0] == "ly" and lenOption == 4:
        lenResult = (float(entry[0])) * 946073047258000000000
        print(f"RESULT: {lenResult:,} cm")
    elif reverseEntry[0] == "ly" and lenOption == 5:
        lenResult = (float(entry[0])) * 9460730472580000000000
        print(f"RESULT: {lenResult:,} mm")
    elif reverseEntry[0] == "ly" and lenOption == 6:
        print("error.. do not choose equal units")


# Main if-elif option chain
if option == 1:
    pressureCalc()
elif option == 2:
    velocityCalc()
elif option == 3:
    tempCalc()
elif option == 4:
    lengthCalc()
elif option == 5:
    print("Leaving......")
else:
    print("Invalid option!")