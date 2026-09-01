#Find the second largest number
#Given a list of numbers, find the second largest number without using sort().

numbers = [12, 45, 7, 34, 89, 23]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second largest:", second_largest)