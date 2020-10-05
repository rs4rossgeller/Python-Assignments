# Question : Menu Driven Program using Linear and Binary Search.
# Language : Python 2.7



def LSearch(L, Element):
    for i in range(len(L)):
        if Element == L[i]:
            print "Element Found at", i+1
            break
    else:
        print "Not Found!"

def BSearch(L, Element):
    Begin = 0
    Last = len(L) - 1
    while Begin <= Last:
        Middle = (Begin+Last)/2

        if Element == L[Middle]:
            print "Found at", Middle
            break

        elif Element > L[Middle]:
            Begin = Middle + 1

        else:
            Last = Middle - 1

    else:
            print "Not Found!"

while True:
    print "1. Linear Search"
    print "2. Binary Search"
    Option = input("Enter Choice                  : ")
    n = input("Enter Number of Elements      : ")
    L = [input("Enter the Element             : ") for i in range(n)]

    if Option == 1:
        x = input("Enter the Element to search   : ")
        LSearch(L, x)

    elif Option == 2:
        x = input("Enter the Element to search   : ")
        BSearch(L,x)

    else:
        print "Invalid Choice!"

    if raw_input("Do you want to continue? 'Yes/No': ").lower() == "no":
        break
