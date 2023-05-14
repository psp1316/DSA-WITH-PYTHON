class Node:
    def __init__ (self,value):
        self.value=value
        self.next=None
        

class stack:
    def __init__ (self,value):    
        newnode=Node(value)
        self.top=newnode
        self.height=1
    
    def printstack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push(self,value):
        newnode=Node(value)
        if self.height is None:
            self.top=newnode
        else:
            newnode.next=self.top
            self.top=newnode 
        self.height+=1     

    def pop(self):
        if self.height is None:
            return None
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None   
            self.height-=1    
            return temp      

mystack=stack(10)
mystack.push(67)
mystack.pop()
mystack.printstack()
