#Sum of Even Numbers
#Write a Python program that:
  #Takes a number n from the user.
  #Uses a loop to find the sum of all even numbers from 1 to n.
  #Prints the final sum.

num = int(input("Enter a number: "))

sum = 0
i = 0

while i <= num:
    if i % 2 == 0:
        sum = sum + i

    i = i + 1

print("Sum of even numbers:", sum)