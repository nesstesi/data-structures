class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.value

class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        current_item = self.head
        return current_item

    def __next__(self):
        current_item = self.head
        if current_item is not None:
            val = current_item.value
            current_item = current_item.next
            return val
        else:
            raise StopIteration

    def add_to_tail(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def add_to_head(self,value):
        node = Node(value)
        if self.head is not None:
            self.head = node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_tail(5)
    linked_list.add_to_tail(10)
    for node in linked_list:
        print(node)
