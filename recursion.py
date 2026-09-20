#When a func calls itself repeatedly.

#recursive function
def show(n):
    if(n == 0): #Base case
        return
    print(n)
    show(n-1)

show(5)

#returns n! 

def fact(x):
    if(x == 1 or x == 1):
        return 1
    return fact(x-1) * x


print(fact(4))