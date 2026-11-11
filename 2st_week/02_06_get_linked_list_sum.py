
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

    # 하나의 LinkedList를 숫자로 변환


def single_linked_sum(linked_list):
    current = linked_list
    number_str = ""

    while current is not None:
        number_str += str(current.data)
        current = current.next

    return int(number_str)

    # 두 LinkedList의 합계 계산
def get_linked_list_sum(linked_list_1, linked_list_2):

    a = single_linked_sum(linked_list_1)
    b = single_linked_sum(linked_list_2)

    return a + b


# 첫 번째 LinkedList
linked_list1 = LinkedList(1)
linked_list1.append(2)
linked_list1.append(3)
linked_list1.append(4)

# 두 번째 LinkedList
linked_list2 = LinkedList(1)
linked_list2.append(2)
linked_list2.append(3)
linked_list2.append(4)

result = get_linked_list_sum(linked_list1.head, linked_list2.head )
print(result)  # 2468
