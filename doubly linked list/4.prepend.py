class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.pre=None
class doublylinkedlist:
    def __init__(self,value):
        newnode=Node(value)
        self.head=newnode
        self.tail=newnode
        self.length=1
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def append(self,value):
        new=Node(value)
        if self.head==None:
            self.head=new
            self.tail=new
        else:   
            self.tail.next=new
            new.pre=self.tail
            self.tail=new
        self.length+=1
    def prepend(self,value):
        new1=Node(value)
        if self.length==0:
            self.head=new1
            self.tail=new1
        else:
            new1.next=self.head
            self.head.pre=new1
            self.head=new1
        self.length+=1

myll=doublylinkedlist(34)
myll.append(56)
myll.prepend(76)
myll.printlist()                
        
