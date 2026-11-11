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
            current =current.next

        current.next = Node(value)

    def print_all(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next
        print()

    def get_node(self, index):
        current = self.head
        current_index = 0

        while current is not None and current_index < index:
            current = current.next
            current_index +=1

        if current is None:
            raise IndexError("인덱스가 범위를 벗어났습니다.")

        print(current.data)

    def add_node(self, data, index):
        current = self.head
        previous_node = None
        current_index = 0

        new_node = Node(data)

        # index가 음수라면 삽입할 수 없음
        if index < 0:
            raise IndexError("인덱스가 음수입니다.")

        while current is not None and current_index < index:
            previous_node = current # 이전 값
            current = current.next # 이후 값
            current_index +=1

        # 리스트 길이를 초과한 위치라면 오류
        if current_index != index:
            raise IndexError("인덱스가 범위를 벗어났습니다.")

            # 첫 번째 위치에 삽입
        if previous_node is None:
            new_node.next = self.head
            self.head = new_node

            # 중간 또는 마지막 위치에 삽입
        else:
            new_node.next = current
            previous_node.next = new_node











linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(13)
linked_list.append(14)

linked_list.get_node(2)

linked_list.print_all()