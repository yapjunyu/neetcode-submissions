# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow becomes our second half
        curr = slow.next
        slow.next = None # cut the first half
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev becomes head of reversed half
        first, second = head, prev
        while second:
            a, b = first.next, second.next
            first.next = second
            second.next = a
            first = a
            second = b
        return second
