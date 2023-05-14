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
    def append(self,value):
        newnode=Node(value)
        if self.length==0:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        self.length+=1
        return True
    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in range(self.length):
            after=temp.next
            temp.next=before
            before=temp
            temp=after

myLL=linkedlist(56)   
myLL.append(67)
myLL.append(78)
print("your linked list is:",myLL.printlist())
myLL.reverse()
print("your reversed linked list is:",myLL.printlist())                 