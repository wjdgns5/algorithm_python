class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(value)

    def print_all(self):
        current = self.head

        while current.next is not None:
            print(current.data, end=" ")
            current = current.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

print(linked_list.print_all())