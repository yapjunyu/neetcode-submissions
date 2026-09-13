# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 pass
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        
        dummy = ListNode(0, head) # use a dummy node to handle head removal easily
        curr = dummy

        for _ in range(length - n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

        
        