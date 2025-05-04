# Problem: Decimal to binary number using recursion - https://www.geeksforgeeks.org/decimal-binary-number-using-recursion/

def decimal_to_binary(d):
    if d == 0:
        return "0"
    if d == 1:
        return "1"
    return decimal_to_binary(d // 2) + str(d % 2)