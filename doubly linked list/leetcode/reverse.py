class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def reverse(self):
        pre=self.head
        while self.head is not None:
            temp=self.head.prev
            self.head.prev=self.head.next
            self.head.next=temp
            self.head=self.head.prev
        pre=self.head    
        self.head=self.tail  
        self.tail=pre
    

my_doubly_linked_list = DoublyLinkedList(45)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(78)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.reverse()


#print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()