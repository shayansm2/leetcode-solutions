class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseNode = None
        
        while head:
            reverseNode = ListNode(head.val, reverseNode)
            head = head.next

        return reverseNode
        
