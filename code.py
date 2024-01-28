# Python program to find the maximum of three numbers

def find_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Taking three numbers as input from the user
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

# Finding the maximum number
max_number = find_max(number1, number2, number3)

# Displaying the result
print(f"The maximum number among {number1}, {number2}, and {number3} is {max_number}")
