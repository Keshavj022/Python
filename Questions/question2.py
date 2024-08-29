# Write a code to check whether a given number is a palindrome.

number = int(input("enter the number"))
temp = number
palindrome = 0

while temp > 0:
    r = temp % 10
    palindrome = palindrome*10 + r
    temp = temp // 10

if number == palindrome:
    print("Palindrome number")
else:
    print("Not a Palindrome Number")
