#Check whether a number reads the same forwards and backwards.

num = int(input("Enter a number: "))

originalNum = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if originalNum == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")