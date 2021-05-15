class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def intersection_check(heada:ListNode, headb:ListNode):
        if heada == None or headb == None: return None

        curr1 = heada
        curr2 = headb

        while curr1 != curr2:
            if curr1 == None:
                curr1 = headb
            else:
                curr1.next
            if curr2 == None:
                curr2 = headb
            else:
                curr2.next

        return curr1.data
