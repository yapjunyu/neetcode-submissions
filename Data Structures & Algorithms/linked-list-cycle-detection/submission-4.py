# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next: # condition should be the faster pointer since it is moving faster than head and can hit none
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False
        