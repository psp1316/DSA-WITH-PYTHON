# class node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
# class linkedlist:
#     def __init__(self,value):
#         newnode=node(value)
#         self.head=newnode
#         self.tail=newnode
#         self.length=1
# mylinkedlist=linkedlist(4)

# print(mylinkedlist.head.value)
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class LinkedList :
    def __init__(self,value):
        myvalue=Node(value)
        self.head=myvalue
        self.tail=myvalue
        self.length=1



# DO NOT EDIT CODE BELOW THIS LINE 
my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

