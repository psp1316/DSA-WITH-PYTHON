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
    def popfirst(self):
        if self.length==0:
            return None
        temp=self.head    
        if self.length==1:
            self.head==None
            self.tail==None    
        else:
            self.head=self.head.next
            self.head.pre=None
            temp.next=None
        self.length-=1
        return temp.value

myll=doublylinkedlist(34)
#myll.append()
myll.popfirst()
myll.printlist()            


        