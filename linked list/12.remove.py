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
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp 
    def prepend(self,value):
        newnode=Node(value)
        if self.length==0:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head=newnode 
        self.length+=1   
        return True 
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

    def pop(self):
        if self.length==0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if(self.length==0):
            self.head=None
            self.tail=None    
        return temp                 

    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.prepend(value)     
        if index==self.length:
            return self.append(value)
        
        newnode=Node(value)
        temp=self.get(index - 1)
        newnode.next=temp.next
        temp.next=newnode
        self.length+=1
        return True

    def remove(self,index):
        if index<0 or index>self.length:
            return False
        if index==0:
            return self.popfirst()
        if index==(index-1):
            return self.pop()        
        temp=self.get(index-1)
        pre=temp.next
        temp.next=pre.next
        pre.next=None
        self.length-=1
        return temp     

myLL=linkedlist(45)
myLL.append(56)
myLL.append(67)
myLL.printlist()
myLL.insert(1 , 54)  
myLL.printlist()
myLL.remove(0)   
myLL.printlist()   


