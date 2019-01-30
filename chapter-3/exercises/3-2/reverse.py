class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # the pointer initially points to nothing

class LinkedList:
    def __init__(self, node):
        self.head = node

    def print_list(self):
        start = self.head
        while start is not None:
            print(start.value)
            start = start.next

    def reverse(self):
        current = self.head
        prev_node = None

        while current.next is not None:
            next_node = current.next
            current.next = prev_node

            prev_node = current
            current = next_node

        current.next = prev_node
        self.head = current

if __name__ == '__main__':
    head = Node(0)
    current_head = head
    for i in range(1, 10):
        current_head.next = Node(i)
        current_head = current_head.next

    link = LinkedList(head)
    link.print_list()

    print()

    link.reverse()
    link.print_list()
