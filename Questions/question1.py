# Write a code to find the minimum among three given numbers.

num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))

minimum = 0

if num1 < num2 and num1 < num3:
    minimum = num1
elif num2 < num1 and num2 < num3:
    minimum = num2

else:
    minimum = num3

print(f"minimum is {minimum}")
