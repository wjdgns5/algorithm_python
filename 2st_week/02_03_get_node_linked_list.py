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

        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def get_node(self, index):
        current = self.head
        number = 0

        while number != index is not None:
            current = current.next
            number += 1

        print(current.data)

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(13)
linked_list.append(14)

linked_list.get_node(2) # -> 5를 들고 있는 노드를 반환해야 합니다!

linked_list.print_all()

