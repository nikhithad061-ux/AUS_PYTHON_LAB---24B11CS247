# Write a Python program that demonstrates error handling using try-except block to handle division by zero.
try:
    num1=int(input("Enter numerator: "))
    num2=int(input("Enter denominator: "))
    result=num1/num2
    print("Result:",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
