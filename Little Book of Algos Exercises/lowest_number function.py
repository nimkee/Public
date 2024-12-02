
def lower_num(num1, num2):
    if num1 <= num2:
        return num1
    else:
        return num2

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

lowest = lower_num(first_num, second_num)

print("The lowest number is " + str(lowest))