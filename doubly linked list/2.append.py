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

myll=doublylinkedlist(76)
myll.append(67)
myll.printlist()           


