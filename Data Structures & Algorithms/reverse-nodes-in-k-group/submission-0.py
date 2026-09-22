# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_grp_tail = dummy
        while self.has_k_nodes(prev_grp_tail.next, k):
            curr = temp = prev_grp_tail.next
            for _ in range(k - 1):
                curr = curr.next
            next_grp = curr.next
            curr.next = None

            new_head = self.reverseList(temp)
            prev_grp_tail.next = new_head
            temp.next = next_grp
            prev_grp_tail = temp
        return dummy.next

    def has_k_nodes(self, head, k):
        count = 0
        curr = head
        while curr and count < k:
            count += 1
            curr = curr.next
        return count == k

    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
