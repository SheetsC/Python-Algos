class Node:
    def __init__(self,val = 0, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random

    def copyRandomList(head):
        if not head: return None

        node_map = {}
        curr = head
        
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head

        while curr:
            if curr.next:
                node_map[curr].next = node_map[curr.next]
            if curr.random:
                node_map[curr].random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]
