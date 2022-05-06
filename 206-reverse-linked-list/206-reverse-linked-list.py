# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(prev, cur):
            if not cur:
                return prev
            x = rec(cur,cur.next)
            cur.next = prev
            return x
        return rec(None,head)
        # iterative
        # prev = None
        # current = head
        # while current:
        #     tmp = current.next
        #     current.next = prev
        #     prev = current
        #     current = tmp
        # return prev
        