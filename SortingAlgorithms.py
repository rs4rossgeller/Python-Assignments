# Menu Driven Program to perform various sorting techniques
# Python2.7

def Bubble_Sort(L):
    for i in range(len(L)-1, 1):
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    print L

def Selection_Sort(L):
    for i in range(len(L)-1):
        small = L[i]
        pos = i
        for j in range(i+1, len(L)):
            if L[j] < small:
                small = L[j]
                pos = j
        L[i], L[pos] = L[pos], L[i]
    print L

def Insertion_Sort(L):
    for i in range(1, len(L)):
        temp = L[i]
        ptr = i-1
        while ptr >= 0 and L[ptr] > temp:
            L[ptr+1] = L[ptr]
            ptr -= 1
        L[ptr+1] = temp
    print L

while True:
    n = input("Enter the Number of Elements             : ")
    L = [input("Enter Element                            : ") for i in range(n)]
    print "1. Bubble Sort"
    print "2. Selection Sort"
    print "3. Insertion Sort"
    Option = input("Enter Choice                             : ")

    if Option == 1:
        Bubble_Sort(L)

    elif Option == 2:
        Selection_Sort(L)

    elif Option == 3:
        Insertion_Sort(L)

    else:
        print "Invalid Choice!"

    if raw_input("Do you wish to continue? 'Yes/No'        : ").lower() == "no":
        break
    print "-------------------------------------------"
