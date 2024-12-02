
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 <= num2:
    lowest = num1
else:
    lowest = num2

print("The lowest number is " + str(lowest))


def lower_num(number1, number2):
    if number1 <= number2:
        lowest = number1
    else:
        lowest = number2

    print(f"The lowest number is {lowest}")

lower_num(25, 36)
