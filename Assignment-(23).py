def isempty(stk):
    if stk == []:
        return True
    else:
        return False
    
def push(stk,item):
    stk.append(item)
    top = len(stk) - 1

def pop(stk):
    if isempty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk) - 1
        return item

def peek(stk):
    if isempty(stk):
        return "Underflow"
    else:
            top = len(stk) - 1
            return stk[top]

def display(stk):
    if isempty(stk):
        print("Stack empty")
    else:
        top = len(stk) - 1
        print(stk[top], "<--- top")
        for a in range(top - 1, -1, -1):
            print(stk[a])
            
#__main__
Stack = []
top = None
while True:
    print("\n\t\t\tSTACK OPERATIONS")
    print("\t\t\t--------------------------\n")
    print("\t1. Push")
    print("\t2. Pop")
    print("\t3. Peek")
    print("\t4. Display stack")
    print("\t5. Exit")
    ch = int(input("\nEnter your choice (1-5): "))
    if ch == 1:
        item = int(input("Enter item:"))
        push(Stack, item)
    elif ch == 2:
        item = pop(Stack)
        if item == "Underflow":
            print("\nUnderflow! Stack is empty!")
        else:
            print("\nPopped item is", item)
    elif ch == 3:
        item = peek(Stack)
        if item == "Underflow":
            print("\nUnderflow! Stack is empty!")
        else:
            print("\nTopmost item is", item)
    elif ch == 4:
        display (Stack)
    elif ch == 5:
        print("\n\rProgram Ended !!!")
        break
    else:
        print("\nInvalid choice.")
    k = input("Do you want to continue ?(y/n):")
    if k == 'y' or k == 'Y':
        continue
    else:
        print("\n\rProgram Ended !!!")
        break







            
