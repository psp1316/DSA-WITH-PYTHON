class Node:
    def __init__ (self,value):    
        self.value=value
        self.next=None

class queue:
    def __init__ (self,value):
        newnode=Node(value)
        self.first=newnode
        self.last=newnode
        self.length=1

    def printlist(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def enqueue(self,value):
        newnode=Node(value)
        if self.length is None:
            self.first=newnode 
            self.last=newnode 
        else:
            self.last.next=newnode
            newnode=self.last
            self.length+=1

    def dequeue(self):
        if self.length is None:
            return None
        else:
            temp=self.first
            self.first=temp.next
            
        self.length-=1
        return temp

myqueue=queue(45)
                   
myqueue.enqueue(67)
myqueue.dequeue()

myqueue.printlist()  