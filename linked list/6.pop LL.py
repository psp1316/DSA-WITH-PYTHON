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
           return True 
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
  
#mylinkedlist=linkedlist(4)      
#mylinkedlist.append(8)
#print(mylinkedlist.pop())
#mylinkedlist.printlist()  

my_linked_list = linkedlist(7)
my_linked_list.append(8)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())