#Three ways to write a string:
print("Free Plestine")
print('All Eyes On Gaza')
print("""From river to the sea Pleastine will be free.""")

#assign a string to a variable :
a = "I am Wasim"
print(a)
#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:

x = """
My name is Wasim and i am studying Bsc.IT from Mumbai University, 
I love to stay at home, dont like to go out much,
In entire life of student i did'nt able to make a Girlefreind,
I hate going College, Thank you!
"""
print(x)

#Strings are arrays.
#Square brackets can be used to access elements of the string.
print(a[3])


#Looping Through a String
#Since strings are arrays, we can loop through the characters in a string, with a for loop.

for i in "KolkataKinghtRiders" :
    print(i)
    
#String Length
#To get the length of a string, use the len() function.

x = "KolkataKinghtRiders"
print("The length of x: ",len(x))

#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword 'in' it returns Boolean Value.

txt = "Wasim is a Hustler."
print("Hustler" in txt)

#Slicing String:

txt2 = "KnightRiders"
print(txt2[0:6])

#Slice From the Start
print(txt2[:6])

#Slice To the End
print(txt2[:11])

#Negative Indexing
#Use negative indexes to start the slice from the end of the string:

print(txt2[-11:-2])

#Modify Strings
#Python has a set of built-in methods that you can use on strings.

#Upper Case
print(txt2.upper())

#Lower Case
print(txt2.lower())

#Remove Whitespace
txt3 = "   I am a Knightrider   "
print(txt3.strip())

#Replace String
#The replace() method replaces a string with another string:

txt4 = "Love KKR"
print(txt4.replace("Love", "Ami"))

#Split String
#The split() method returns a list where the text between the specified separator becomes the list items.

txt5 = "Hello, Python"
print(txt5.split(","))

#String Concatenation
#To concatenate, or combine, two strings you can use the + operator.

n = "Hala"
h = "Madrid"
c = n+h

print(c)

#F-Strings
#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
#A placeholder can contain variables, operations, functions, and modifiers to format the value.

age = 21
txt6 = f"My name is Wasim and my age is {age}"
print(txt6)