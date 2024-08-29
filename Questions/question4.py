# A three-digit number is said to be an “Armstrong number” if the sum of the third power of its individual digits is
# equal to the number itself.Write a program to check whether a number is armstrong or not.

number = int(input("enter a three-digit number"))
temp = number
count_digits = 0
armstrong = 0
while temp > 0:
    count_digits += 1
    r = temp % 10
    armstrong += r ** 3
    temp = temp // 10

if count_digits == 3:
    if armstrong == number:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

else:
    print("Please enter three digit number")
