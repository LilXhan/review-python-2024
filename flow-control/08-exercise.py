print("Welcome to the calculator!")
print("To exit write exit.")
print("The operations are sum, multi, div and subtract.")

total = ""
while True:
    if not total and total != 0:
        total = input("Enter a number: ").lower().strip()
        if total == "exit":
            break
        total = int(total)
    operation = input("Choice a operation: ").lower().strip()
    if operation == "exit":
        break
    number = input("Enter a next number: ").lower().strip()
    if number == "exit":
        break
    number = int(number)
    total = int(total)
    if operation == "sum":
        total += number
        print(f"The result is {total}.")
    elif operation == "multi":
        total *= number
        print(f"The result is {total}.")
    elif operation == "div":
        total /= number
        print(f"The result is {total}.")
    elif operation == "subtract":
        total -= number
        print(f"The result is {total}.")
    else:
        print("enter a valid operation")
        break