from typing import Optional


class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int):
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head.next if head and head.val == val else head

        