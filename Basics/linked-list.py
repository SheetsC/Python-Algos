class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, ):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def make_list(self):
        list_of_links = []
        current = self.head
        while current is not None:
            list_of_links.append(current.value)
            current = current.next
        return list_of_links
    
    def get_newest_first(self):
        newest_first = self.make_list()
        newest_first.reverse()
        return newest_first


