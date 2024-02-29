from node import Node
from polynomial import Polynomial

class Circular_list:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def insert_at_beginning(self, data:int): # Method to add components to the polynomial
        new_node = Node(Polynomial(data,self.size,'x'))
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.size += 1
        else:
            last_node = self.get_last_node()
            last_node.next = new_node
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def show_list(self):
        current = self.head
        if current == None:
            print("The list is empty\n")
            return
        print(current.data, end="")
        current = current.next
        while current != self.head:
            print(current.data, end="")
            current = current.next
        print()

    def get_last_node(self):
        current = self.head
        while current.next != self.head:
            current = current.next
        return current
    
    def evaluate_polynomial(self,data:int):
        self.head.data.var = data
        current = self.head
        if current == None:
            print("The list is empty\n")
            return
        print(current.data, end="")
        current = current.next
        while current != self.head:
            print(current.data, end="")
            current = current.next
        print()
