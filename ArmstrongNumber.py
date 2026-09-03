num = int(input("Enter a number: "))

original_num = num
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** 3
    num = num // 10

if original_num == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")