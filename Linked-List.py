'''This will prompt the user to input the number of elements 
they want to add to the linked list, and then for each element,
 it will ask the user to input the element. After all the elements 
have been added, it will print the linked list.'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

ll = LinkedList()

num_elements = int(input("Enter the number of elements you want to add to the linked list: "))

for i in range(num_elements):
    element = input("Enter element: ")
    ll.append(element)

print("Linked List:")
ll.print_list()
