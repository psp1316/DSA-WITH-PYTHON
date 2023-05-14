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
    def get(self,index):
        if index<0 or index>self.length:
            return None
        temp=self.head    
        if index<self.length/2:
            for _ in range(index):
                temp=temp.next
            return temp
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.pre
            return temp.value

myll=doublylinkedlist(87)
myll.append(78)
myll.append(567)
print(myll.get(2))
            


