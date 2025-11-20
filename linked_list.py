# Creating a node Class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        #LinkedList.traverse()

# Implement Linked List
class LinkedList:
    def __init__(self):
        self.head=None
        

# Add nodes
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        self.traverse()

    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        self.traverse()

    def insert_at_position(self,data,position):
        if position==0:
            self.insert_at_beginning(data) 
            return
        new_node=Node(data)
        current=self.head
        for _ in range(position-1):
            if not current:
                print("position ouf of bounds")
                return
            current=current.next
        new_node.next=current.next
        current.next=new_node
        self.traverse()

    # Deleting a Value
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
        self.traverse()
        
    def delete_by_position(self,position):
        if not self.head:
            return
        if position==0:
            self.head=self.head.next
            return
        current=self.head
        for _ in range(position-1):
            if not current or not current.next:
                print("Position out of bounds")
                return
            current=current.next
            if current.next:
                current.next=current.next.next
        self.traverse()

    # Transverse the Linked list
    def traverse(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")

# Create a linked list and perform operations
llist=LinkedList()
llist.insert_at_beginning(10)
llist.insert_at_end(20)
llist.insert_at_position(15,1)
llist.delete_by_value(15)
llist.delete_by_position(0)
llist.traverse()



    



