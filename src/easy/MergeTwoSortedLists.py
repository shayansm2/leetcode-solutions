from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        current = self
        string = '['

        while current:
            string += (str(current.val) + ',')
            current = current.next

        string += ']'

        return string


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        merged = ListNode()
        current = merged

        while l1 is not None and l2 is not None:
            val1 = l1.val
            val2 = l2.val

            if val1 <= val2:
                current.val = val1
                l1 = l1.next
            else:
                current.val = val2
                l2 = l2.next

            current.next = ListNode()
            current = current.next

        if l1 is None:
            current.val = l2.val
            current.next = l2.next

        if l2 is None:
            current.val = l1.val
            current.next = l1.next

        return merged


# l1 = ListNode(1, ListNode(2, ListNode(4)))
# l2 = ListNode(1, ListNode(3, ListNode(4)))

l1 = ListNode(2)
l2 = ListNode(1)

print(Solution().mergeTwoLists(l1, l2))
