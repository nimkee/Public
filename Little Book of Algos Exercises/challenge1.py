import random as r
# Challenge 1: Highest Number

def highest_number(num1, num2, num3):
    highest = num1
    if num2 > highest:
        highest = num2
    if num3 > highest:
        highest = num3
    return highest

print(highest_number(9000, 223, 50))













def max_list(list):
    if not list:
        return None

    else:
        highest = list[0]
        for num in list:
            if num >= highest:
                highest = num

        return highest


min_val = 0
max_val = 1000
list_length = 20

my_list = list(r.randint(min_val, max_val) for _ in range(list_length))
print(my_list)
print(max_list(my_list))

