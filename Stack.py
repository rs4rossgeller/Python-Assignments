# Question : Menu-Driven Program to implement a Stack using list and classes
# Python2.7

class Stack:
    s = []

    def Push(self):
        self.Element = input("Enter the Element                : ")
        Stack.s.append([self.Element])

    def Pop(self):
        if not Stack.s:
            print "UnderFlow"
        else:
            print "Deleted Element", Stack.s.pop()

    def Display(self):
        if not Stack.s:
            print 'Empty Stack'
        else:
            print "Information"
            for i in range(len(Stack.s)-1, -1, -1):
                print Stack.s[i]

x = Stack()
while True:
    print "1. Push"
    print "2. Pop"
    print "3. Display"
    Option = input("Enter your Choice               : ")

    if Option == 1:
        x.Push()
    elif Option == 2:
        x.Pop()
    elif Option == 3:
        x.Display()
    if raw_input("Do you want to continue? 'Yes/No' : ").lower() == "no":
        break
