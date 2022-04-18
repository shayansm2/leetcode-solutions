from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        summation = root

        additionalOne = 0
        while l1 or l2 or additionalOne:
            summation.next = ListNode()
            summation = summation.next

            sumOfElements = 0

            if additionalOne:
                sumOfElements += 1
                additionalOne = 0

            if l1:
                sumOfElements += l1.val
                l1 = l1.next

            if l2:
                sumOfElements += l2.val
                l2 = l2.next

            if sumOfElements > 9:
                additionalOne = 1
                sumOfElements %= 10

            summation.val = sumOfElements
        return root.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        p, q, curr = l1, l2, dummyHead
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            summation = carry + x + y
            carry = summation // 10
            curr.next = ListNode(summation % 10)
            curr = curr.next
            if p: p = p.next
            if q: q = q.next
        if carry:
            curr.next = ListNode(carry)
        return dummyHead.next
