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

    def get(self,index):
        if index<0 or index>self.length:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp.value

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

         
                

myLL=linkedlist(89)
myLL.append(678)   
myLL.append(68) 
myLL.append(698) 
myLL.append(567) 
myLL.append(34) 
myLL.printlist()   
          
print("your index value is:", myLL.get(4))






        