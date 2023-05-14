class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:
    def __init__(self,value):
        myvalue=Node(value)
        self.head=myvalue
        self.tail=myvalue
        self.length=1

    def append(self, value):
        newnode=Node(value)
        if(self.head is None):
           self.head=newnode
           self.tail=newnode
        else:
           self.tail.next=newnode
           self.tail=newnode
           self.length+=1   

    def prepend(self,value):
        newnode=Node(value)
        if self.length==0:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode 
        self.length+=1

    def popfirst(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp    

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next   

mylinkedlist=linkedlist(65)
mylinkedlist.append(67)
mylinkedlist.prepend(56)
mylinkedlist.printlist()
mylinkedlist.popfirst()            
mylinkedlist.printlist()