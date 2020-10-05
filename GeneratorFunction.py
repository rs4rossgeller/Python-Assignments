# Question : Menu Driven Program using generator functions
# Python2.7

def Fibonacci(n):
    a = 0
    b = 1
    yield a
    yield b
    for i in range(1, n-1):
        c = a + b
        yield c
        a, b = b, c

def OddSquare(n):
    for i in range(1, n+1, 2):
        yield i ** 2

def EvenCube(n):
    for i in range(2, n+1, 2):
        yield i ** 3

while True:
    print "------------------------------"
    print """
1. Fibonacci
2. OddSquares
3. EvenCubes"""
    Option = input("Enter Choice               : ")

    if Option==1:
        x = input("Enter the Limit            : ")
        gn=Fibonacci(x)
        for i in Fibonacci(x):
            print i,

    elif Option==2:
        y = input("Enter the Limit            : ")
        gn=OddSquare(y)
        for i in OddSquare(y):
            print i,

    elif Option==3:
        z = input("Enter the Limit: ")
        gn = EvenCube(z)
        for i in EvenCube(z):
            print i,

    else:
        print "Invalid Choice!"
    if raw_input("\nDo you want to continue? 'Yes/No': ").lower() == "no":
        break
