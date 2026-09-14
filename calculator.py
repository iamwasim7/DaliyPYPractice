print("Welcome to calculator!")
num1 = input("Enter 1st number:")
oprator = input("Enter a opreator:")
num2 = input("Enter 2nd number:")

if oprator == "+" :
    print("The value of", num1, "+", num2, "is", int(num1)+int(num2))

elif oprator == "-" :
    print("The value of", num1, "-", num2, "is", int(num1)-int(num2))

elif oprator == "*" :
    print("The value of", num1, "*", num2, "is", int(num1)*int(num2))

elif oprator == "/" :
    print("The value of", num1, "/", num2, "is", int(num1)/int(num2))

elif oprator == "%" :
    print("The value of", num1, "%", num2, "is", int(num1)%int(num2))