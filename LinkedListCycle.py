class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow_p = self.head
        fast_p = self.head

        while (fast_p and fast_p.next):
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if fast_p is slow_p:
                return True
        return False
