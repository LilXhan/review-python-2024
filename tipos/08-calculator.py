print("----CALCULATOR-----")
print("1) Addition")
print("2) Subtraction")
print("3) Division")
print("4) Multiplication")
chosen_option = int(input("Choose and option: \n"))
print(type(chosen_option))
if chosen_option == 1:
    print("Addition")
    number1 = int(input("Enter the first number: \n"))
    number2 = int(input("Enter the second number: \n"))
    print(f"Result is {number1 + number2}")
elif chosen_option == 2: 
    print("Subtraction")
    number1 = int(input("Enter the first number: \n"))
    number2 = int(input("Enter the second number: \n"))
    print(f"Result is {number1 - number2}")
elif chosen_option == 3:
    print("Division")
    number1 = int(input("Enter the first number: \n"))
    number2 = int(input("Enter the second number: \n"))
    while number1 == 0 or number2 == 0:
        print("Zero is invalid, choose a other number.")
        number1 = int(input("Enter the first number: \n"))
        number2 = int(input("Enter the second number: \n"))
    print(f"Result is {number1 / number2}")
elif chosen_option == 4:
    print("Multiplication")
    number1 = int(input("Enter the first number: \n"))
    number2 = int(input("Enter the second number: \n"))
    print(f"Result is {number1 * number2}")
else:
    print("Invalid option")