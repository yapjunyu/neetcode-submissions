# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        carry = 0
        while l1 or l2:
            add = carry
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            node1 = ListNode(add % 10)
            res.next = node1
            res = res.next
            # if created a new node in prev loop, no need to create a new one just update
            if add >= 10:
                carry = 1
            else:
                carry = 0
        if carry:
            res.next = ListNode(1)
        return dummy.next
