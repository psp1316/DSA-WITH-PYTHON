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

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self, value):
        newnode=Node(value)
        if(self.head is None):
           self.head=newnode
           self.tail=newnode
        else:
           self.tail.next=newnode
           self.tail=newnode
           self.length+=1   

mylinkedlist=linkedlist(4)      
mylinkedlist.append(8)
mylinkedlist.printlist()  
