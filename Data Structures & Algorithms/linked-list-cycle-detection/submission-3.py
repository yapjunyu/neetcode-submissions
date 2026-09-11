# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hmap = {}
        count = 0
        while head:
            if head.next == None:
                return False
            head = head.next
            if head.val not in hmap:
                hmap[head.val] = 'a'
            else:
                return True
        return False
        