# Creating a Node Class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# implementing a Linked List
class LinkedList:
    def __init__(self):
        self.head=None

# Adding Nodes
# a. insert at the beginning
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

# b. insert at the end
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

# c. insert at a Specific Position
    def insert_at_position(self,data,position):
        if position==0:
            self.insert_at_beginning(data)
            return
        new_node=Node(data)
        current=self.head
        for _ in range(position-1):
            if not current:
                print("Position out of bounds")
                return
            current=current.next
        new_node.next=current.next
        current.next=new_node

# Deleteing Nodes
#   a. Delete by Value
    def delete_by_value(self,value):
        if not self.head:
            return
        if self.head.data==value:
            self.head=self.head.next
            return
        current=self.head
        while current.next and current.next.data !=value:
            current=current.next
        if current.next:
            current.next=current.next.next

#   b. delete by position
    def delete_by_position(self,position):
        if not self.head:
            return
        if position==0:
            self.head=self.head.next
            return
        current=self.head
        for _ in range(position-1):
            if not current or not current.next:
                print("Positon out of bounds")
                return
            current=current.next
        if current.next:
            current.next=current.next.next

#Traversing the Linked List
    def traverse(self):
        current=self.head
        number=0
        while current:
            print(f"[{number}] {current.data}",end=" → ")
            current=current.next
            number +=1 
        print("None")

# Example
# Create a linked list and perform operations
llist=LinkedList()
llist.insert_at_beginning(10)
llist.insert_at_end(20)
llist.insert_at_position(15,1)
llist.traverse()

llist.delete_by_value(15)
llist.traverse()

llist.delete_by_position(0)
llist.traverse()

