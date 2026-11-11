class Node:

    def __init__(self, data):
        self.data = data # 값
        self.next = None # 주소

class LinkedList:

    def __init__(self, value):
        self.head = Node(value) # Linked_List 첫번째 Node() 값을 head로 지정.

    def append(self, value):
        current = self.head # 추가하려면  head를 기준으로 시작해야 함.

        while current.next is not None: # head 다음 Node() 값이 null 이 아니라면.
            current = current.next # head.next 값을 current에 입력. (None 나올때 까지 반복)
        current.next = Node(value) # Node가 None 앞 까지, 이동 후, current.next 는 None 이기에, Node(value) 값을 넣는다.

    def print_all(self):
        current = self.head # 조회하려면 head를 기준으로 시작해야 함.

        while current is not None: # head 다음 Node() 값이 null 이 아니라면.
            print(current.data, end=" ") # Node() 현재 값 출력
            current = current.next  # head.next 값을 current에 입력. (None 나올때 까지 반복)

linked_list = LinkedList(1)

linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_all()