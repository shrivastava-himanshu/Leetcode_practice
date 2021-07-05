class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr , prev = head , None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        return prev
    



# 1 2 3 4 5