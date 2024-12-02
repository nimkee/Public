def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_num = ""
    while n > 0:
        binary_num = str(n % 2) + binary_num
        n = n // 2
    return binary_num

# Example usage:
decimal_number = 42
binary_number = decimal_to_binary(decimal_number)
print(f"Decimal: {decimal_number} -> Binary: {binary_number}")
