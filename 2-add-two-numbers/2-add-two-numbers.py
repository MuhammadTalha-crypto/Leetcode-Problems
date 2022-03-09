# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        carry = 0
        currentNode = dummyHead
        while l1 or l2:
            if l1:
                l1_value = l1.val
            else:
                l1_value = 0
            if l2:
                l2_value = l2.val
            else:
                l2_value = 0
                
            sum_ = l1_value + l2_value + carry
            currentNode.next = ListNode(sum_ % 10)
            currentNode = currentNode.next
            carry = sum_  // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            currentNode.next = ListNode(carry)
        return dummyHead.next
        
                
        