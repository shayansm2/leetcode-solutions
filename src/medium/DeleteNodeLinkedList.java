package medium;

import lib.ListNode;

public class DeleteNodeLinkedList {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
