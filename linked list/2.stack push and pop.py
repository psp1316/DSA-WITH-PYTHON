stack=[]
def push():
    element=int(input("enter the number you want to add!!"))
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:    
        e=stack.pop() 
        print(stack)   
while True:
    number=int(input("enter your choice, 1 to push, 2 to pop, 3 to quit\n"))
    if(number==1):
        push()
    elif(number==2):
        pop()
    elif(number==3):
        break
    else:
        print("wrong input")
