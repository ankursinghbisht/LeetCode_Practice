# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        it = head

        carry = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + carry
            carry = val // 10
            temp = ListNode(val % 10)
            it.next = temp
            it = it.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            val = l1.val + carry
            carry = val // 10
            it.next = ListNode(val % 10)
            it = it.next
            l1 = l1.next

        while l2 is not None:
            val = l2.val + carry
            carry = val // 10
            it.next = ListNode(val % 10)
            it = it.next
            l2 = l2.next

        if carry > 0:
            it.next = ListNode(carry)

        return head.next