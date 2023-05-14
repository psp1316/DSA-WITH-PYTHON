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

    def setnode(self,index,value):
        if index<0 or index>self.length:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            temp.value=value    
            return temp.value       

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next 

myLL=linkedlist(45)
myLL.append(78)
myLL.append(56)
myLL.append(23)
myLL.append(98)
myLL.setnode(2,678)
myLL.printlist()

