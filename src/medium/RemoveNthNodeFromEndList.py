# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        length = 0
        node = head
        while node:
            node = node.next
            length += 1

        number_of_next = length - n

        if number_of_next == 0:
            return head.next

        node = head

        for i in range(number_of_next - 1):
            node = node.next

        node.next = node.next.next

        return head
