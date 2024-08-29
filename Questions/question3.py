# Write a code to find the sum of numbers divisible by 4.The code must allow the user to accept a number and add it to
# the sum if it is divisible by 4. It should continue accepting numbers as long as the user wants to provide an input
# and should display the final sum.

sum = 0
while True:
    number = int(input("enter the number"))
    if number % 4 == 0:
        sum += number
        print(sum)
    else:
        print(sum)
