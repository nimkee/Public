# First go at this

bv = input("Please enter a binary number: ")

power = len(bv) - 1
dv = 0

for bit in bv:
    if bit == '1':
        dv += 2** power
    power -= 1 # In a flow chart can check for is power < 0



print(f"The corresponding denary value is: \n\t {dv}.")


